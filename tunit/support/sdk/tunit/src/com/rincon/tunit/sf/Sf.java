package com.rincon.tunit.sf;

/*
 * Copyright (c) 2005-2006 Rincon Research Corporation
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * - Redistributions of source code must retain the above copyright
 *   notice, this list of conditions and the following disclaimer.
 * - Redistributions in binary form must reproduce the above copyright
 *   notice, this list of conditions and the following disclaimer in the
 *   documentation and/or other materials provided with the
 *   distribution.
 * - Neither the name of the Rincon Research Corporation nor the names of
 *   its contributors may be used to endorse or promote products derived
 *   from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 * FOR A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE
 * RINCON RESEARCH OR ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
 * STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
 * OF THE POSSIBILITY OF SUCH DAMAGE
 */

import java.io.IOException;

import org.apache.log4j.Logger;

import net.tinyos.packet.PhoenixError;
import net.tinyos.util.Messenger;

import com.rincon.tunit.sf.SerialForwarder;
import com.rincon.tunit.sf.SfProvider;

/**
 * A Serial Forwarder for a standalone Java application
 * 
 * @author David Moss
 * 
 */
public class Sf implements SerialForwarder, Messenger, PhoenixError {

  /** Logging */
  private static Logger log = Logger.getLogger(Sf.class);

  /** Provider of the serial connection */
  private SfProvider provider;

  /** Motecom to connect with */
  private String motecom;

  /** Port to provide external access through */
  private int port;

  /** Error handler */
  private PhoenixError errorListener;

  /** Messenge handler */
  private Messenger messenger;

  /** True if the serial port is connected */
  private boolean serverRunning;

  /** True if we detected an error */
  private boolean error;
  
  /**
   * Constructor, provide your own message handler
   * 
   * @param myMotecom
   * @param myPort
   * @param errorHandler
   */
  public Sf(String myMotecom, int myPort, Messenger sfMessenger,
      PhoenixError myErrorListener) {
    log = Logger.getLogger(getClass());
    motecom = myMotecom;
    port = myPort;
    messenger = sfMessenger;
    errorListener = myErrorListener;
    connect();
  }

  /**
   * Constructor with the default messenger
   * 
   * @param myMotecom
   * @param myPort
   * @param errorHandler
   */
  public Sf(String myMotecom, int myPort, PhoenixError myErrorListener) {
    log = Logger.getLogger(getClass());
    motecom = myMotecom;
    port = myPort;
    messenger = null;
    errorListener = myErrorListener;
    connect();
  }

  public void incrementClients() {
  }

  public void decrementClients() {
  }

  public void incrementPacketsWritten() {
  }

  public void incrementPacketsRead() {
  }

  public boolean isConnected() {
    return serverRunning;
  }
  
  public void connect() {
    if (provider == null) {
      provider = new SfProvider(motecom, port, this, this, this);
      provider.start();

      error = false;
      synchronized (this) {
        // We wait for a message to come back saying "resynchronizing"
        // to know we're connected.
        
        // I commented out the while loop here because sometimes a missing
        // mote wouldn't produce any feedback indicating that it did or didn't
        // connect.  This should be investigated further.
        while (!serverRunning && !error) {
          try {
            wait(2000);
          } catch (InterruptedException e) {
            e.printStackTrace();
          }
        }
      }
    }
  }

  public void disconnect() {
    if (provider != null) {
      provider.shutdown();
    }

    synchronized (this) {
      // Experiments show we should wait for everything to clear up
      while (serverRunning) {
        try {
          wait();
        } catch (InterruptedException e) {
          e.printStackTrace();
        }
      }
    }
    
    // TODO This is hack-ish.  If we disconnect and decide to reconnect
    // too quickly, the serial driver craps.  I've spent several days
    // trying to fix the java serial driver to let it connect and disconnect
    // from one or multiple nodes, and I think at this point I'm calling it
    // quits since this lets my JUnit tests pass.
    synchronized (this) {
      try {
        wait(500);
      } catch (InterruptedException e) {
        e.printStackTrace();
      }
    }
  }

  public void serverStopped() {
    log.debug(motecom + "." + port + ": server stopped");
    provider = null;
    synchronized (this) {
      serverRunning = false;
      this.notify();
    }
  }

  /**
   * Default SF Messenger handler via Messenger interface
   */
  public void message(String s) {
    log.debug(motecom + "." + port + ": " + s);
    
    if(messenger != null) {
      messenger.message(s);
    }
    
    if (s.contains("resynch")) {
      synchronized (this) {
        serverRunning = true;
        this.notify();
      }
    }
    
    if(s.toLowerCase().contains("error")) {
      error = true;
      this.notify();
    }
  }

  public void error(IOException e) {
    error = true;
    provider.shutdown();
    errorListener.error(e);
    synchronized (this) {
      this.notify();
    }
  }
}