// $Id$

/*
 * Copyright (c) 2004-2005 Crossbow Technology, Inc.  All rights reserved.
 *
 * Permission to use, copy, modify, and distribute this software and its
 * documentation for any purpose, without fee, and without written agreement is
 * hereby granted, provided that the above copyright notice, the following
 * two paragraphs and the author appear in all copies of this software.
 * 
 * IN NO EVENT SHALL CROSSBOW TECHNOLOGY OR ANY OF ITS LICENSORS BE LIABLE TO 
 * ANY PARTY FOR DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL 
 * DAMAGES ARISING OUT OF THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION, EVEN
 * IF CROSSBOW OR ITS LICENSOR HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH 
 * DAMAGE. 
 *
 * CROSSBOW TECHNOLOGY AND ITS LICENSORS SPECIFICALLY DISCLAIM ALL WARRANTIES,
 * INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY 
 * AND FITNESS FOR A PARTICULAR PURPOSE. THE SOFTWARE PROVIDED HEREUNDER IS 
 * ON AN "AS IS" BASIS, AND NEITHER CROSSBOW NOR ANY LICENSOR HAS ANY 
 * OBLIGATION TO PROVIDE MAINTENANCE, SUPPORT, UPDATES, ENHANCEMENTS, OR 
 * MODIFICATIONS.
 */

/// @author Martin Turon <mturon@xbow.com>
/// @author David Gay <dgay@intel-research.net>

/**
 * Generic pin access for pins mapped into I/O space (for which the sbi, cbi
 * instructions give atomic updates). This can be used for ports A-E.
 */

/**
 * "Copyright (c) 2007 CENTRE FOR ELECTRONICS AND DESIGN TECHNOLOGY,IISc.
 *  All rights reserved.
 *
 * Permission to use, copy, modify, and distribute this software and
 * its documentation for any purpose, without fee, and without written
 * agreement is hereby granted, provided that the above copyright
 * notice, the following two paragraphs and the author appear in all
 * copies of this software.
 *
 * IN NO EVENT SHALL CENTRE FOR ELECTRONICS AND DESIGN TECHNOLOGY,IISc BE LIABLE TO
 * ANY PARTY FOR DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES
 * ARISING OUT OF THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION, EVEN
 * IF CENTRE FOR ELECTRONICS AND DESIGN TECHNOLOGY,IISc HAS BEEN ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 *
 * CENTRE FOR ELECTRONICS AND DESIGN TECHNOLOGY,IISc SPECIFICALLY DISCLAIMS
 * ANY WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  THE SOFTWARE
 * PROVIDED HEREUNDER IS ON AN "AS IS" BASIS, AND CENTRE FOR ELECTRONICS
 * AND DESIGN TECHNOLOGY,IISc HAS NO OBLIGATION TO PROVIDE MAINTENANCE,
 * SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS."
 *
 */
 
/**
 * Leds Energy Estimator
 *
 * @author Venkatesh S
 * @author Prabhakar T V
 */

generic module HplAtm128GeneralIOPinP (uint8_t port_addr, 
				 uint8_t ddr_addr, 
				 uint8_t pin_addr,
				 uint8_t bit)
{
  provides interface GeneralIO as IO;
  uses interface Atm128SimEnergyEstimator;
}
implementation
{
#define pin  pin_addr
#define port port_addr
#define ddr  ddr_addr
  sim_time_t t1=0, t2=0, t3=0, t4=0, totalSet=0, totalClear=0;
  bool setFlag = FALSE;
  bool clearFlag = FALSE;
  bool flip = TRUE;
    
  inline async command bool IO.get()        { return READ_BIT (port, bit); }
  inline async command void IO.set()        {
    dbg("Pins", "Setting bit %i of port %i.\n", (int)bit, (int)port);
    SET_BIT  (port, bit);
    if(!setFlag) {
      t1 = sim_time();
      totalSet = t1-t2;
      call Atm128SimEnergyEstimator.setCompute((uint8_t)port,(uint8_t)bit,totalSet);
      setFlag = TRUE;
      clearFlag = FALSE;
    }    
  }
  inline async command void IO.clr()        { 
    CLR_BIT  (port, bit); 
    if(!clearFlag){
      t2 = sim_time();
      totalClear = t2-t1;
      call Atm128SimEnergyEstimator.clearCompute((uint8_t)port,(uint8_t)bit,totalClear);
      t1=t2;
      setFlag = FALSE;
      clearFlag = TRUE;
    }    
  }
  inline async command void IO.toggle()     { 
    atomic FLIP_BIT (port, bit); 
    if(!flip) {
      t4= sim_time();
      totalClear = t4-t3;
      call Atm128SimEnergyEstimator.clearCompute((uint8_t)port,(uint8_t)bit,totalClear);
      t3 = t4;
      atomic flip = TRUE;
    }
    else {
      t3 = sim_time();
      totalSet = t3-t4;
      call Atm128SimEnergyEstimator.setCompute((uint8_t)port,(uint8_t)bit,totalSet);
      atomic flip = FALSE;
    }    
  }
    
  inline async command void IO.makeInput()  { CLR_BIT  (ddr, bit);  }
  inline async command void IO.makeOutput() { SET_BIT  (ddr, bit);  }
  inline async command bool IO.isInput() { return !READ_BIT  (ddr, bit);  }
  inline async command bool IO.isOutput() { return READ_BIT  (ddr, bit);  }
}

