/*
* Copyright (c) 2008 Stanford University. All rights reserved.
* This file may be distributed under the terms of the GNU General
* Public License, version 2.
*/
/**
 * @brief Driver module for the OmniVision OV7670 Camera, inspired by V4L2
 *        linux driver for OV7670.
 * @author Brano Kusy (branislav.kusy@gmail.com)
 */

#include "OV7670.h"
#include "SCCB.h"


module HplOV7670M
{
  provides interface HplOV7670;
  provides interface HplOV7670Advanced;

  uses interface Leds;
  uses interface HplSCCB as Sccb_OVWRITE;
  uses interface GeneralIO as LED;
  uses interface GeneralIO as PWDN;
  uses interface GeneralIO as RESET;
  uses interface GeneralIO as SIOD;
  uses interface GeneralIO as SIOC;
}

implementation {
		int j,i;
	ov_stat_t global_stat;
	uint8_t init_array_qcif[][2] = {
	/*
	 * Set the hardware window.  These values from OV don't entirely
	 * make sense - hstop is less than hstart.  But they work...
	 */

	}; 	
	
	
	/**
	 * (Busy) wait <code>usec</code> microseconds
	 */
	inline void TOSH_uwait(uint16_t usec)
	{
	  uint32_t start,mark = usec;
	
	  //in order to avoid having to reset OSCR0, we need to look at time differences
	
	  start = OSCR0;
	  mark <<= 2;
	  mark *= 13;
	  mark >>= 2;
	
	  //OSCR0-start should work correctly due to nice properties of underflow
	  while ( (OSCR0 - start) < mark);
	}
	
	command uint8_t HplOV7670Advanced.get_reg_val(uint8_t addr)
	{
		uint8_t val;
		call Sccb_OVWRITE.two_write(addr);
		call Sccb_OVWRITE.read(&val);	// Check return status ??
	
		return val;
	}
	
	command uint8_t HplOV7670Advanced.set_reg_val(uint8_t addr, uint8_t reg_val)
	{
		call Sccb_OVWRITE.three_write(reg_val, addr);
	
		return call HplOV7670Advanced.get_reg_val(addr);
	}
	
	command ov_stat_t HplOV7670Advanced.get_ov_stat()
	{
		return global_stat;
	}
	
	command error_t HplOV7670.set_config(ov_config_t *config,uint8_t img_size)
	{
		call HplOV7670.soft_reset();
		switch (config->config) 
		{
			case OV_CONFIG_YUV: 
			{
				call HplOV7670.config_yuv(img_size);
				break;
			}
			case OV_CONFIG_RGB: 
			{
				call HplOV7670.config_rgb();
				break;
			}
			default:
				return FAIL;
		}
		return SUCCESS;
	}
	
	command error_t HplOV7670.init(uint8_t color, uint8_t type,uint8_t img_size)
	{
		led_out();//call LED.makeOutput();
		atomic {
		  if (type == 0) {
			call HplOV7670.hardware_init();
			call HplOV7670.hard_reset();
			call HplOV7670.soft_reset();
		}
			if (color == COLOR_RGB565) 
				call HplOV7670.config_rgb();
			else 
				call HplOV7670.config_yuv(img_size);
		}
		return SUCCESS;
	}
	
	command void HplOV7670.hardware_init()
	{
		pwdn_out();//call PWDN.makeOutput();
		reset_out();//call RESET.makeOutput();
		sdata_out();//call SIOD.makeOutput(); // done by SCCB
		sclock_out();//call SIOC.makeOutput();
	}
	
	command void HplOV7670.hard_reset()
	{
		pwdn_set();//call PWDN.set(); 			// Turn off the camera - PWDN is active high
		//reset_clr();//call RESET.clr();			// lower the hardware reset signal - RESET is active high
		reset_set();
		TOSH_uwait(PWDN_INTERVAL);
	
		pwdn_clr();//call PWDN.clr(); 			// Turn on the camera
		//reset_set();//call RESET.set();			// raise the hardware reset signal
		reset_clr();
		TOSH_uwait(RESET_INTERVAL);
	
		//reset_clr();//call RESET.clr();			// lower the hardware reset signal
		reset_set();
		TOSH_uwait(CRYSTAL_INTERVAL);
	}
	
	command void HplOV7670.soft_reset()
	{
		call Sccb_OVWRITE.init(); //this component is wired to OVWRITE
		call Sccb_OVWRITE.three_write(COM7_RESET,REG_COM7);		//! Software Reset the Camera
		TOSH_uwait(CRYSTAL_INTERVAL);	// wait for camera to settle
		//call Sccb_OVWRITE.three_write(COM7_FMT_QVGA,REG_COM7); 	// QVGA
//		call Sccb_OVWRITE.three_write(COM13_GAMMA|COM13_UVSAT,REG_COM13);
		//call Sccb_OVWRITE.three_write(0x40,COML);	// gate PCLK with HREF
		//call Sccb_OVWRITE.three_write(COM10_PCLK_HB,REG_COM10);	// gate PCLK with HREF
	}
	
	command void HplOV7670.config_yuv(uint8_t img_size)
	{
		// BW IMAGE
	   if(img_size==SIZE_VGA) call Sccb_OVWRITE.three_write(COM7_FMT_VGA, REG_COM7);
	  else call Sccb_OVWRITE.three_write(COM7_FMT_QVGA, REG_COM7);
	  //call Sccb_OVWRITE.three_write(0,REG_RGB444); 	// no RGB 444
	  //call Sccb_OVWRITE.three_write(0,REG_COM1); 	//
	  //call Sccb_OVWRITE.three_write(COM15_R00FF,REG_COM15); 	//
	  //call Sccb_OVWRITE.three_write(0x18,REG_COM9); /* 4x gain ceiling; 0x8 is reserved bit */
	  //call Sccb_OVWRITE.three_write(0x80,0x4f);
	  //call Sccb_OVWRITE.three_write(0x80,0x50);
	  //call Sccb_OVWRITE.three_write(0,0x51);
	  //call Sccb_OVWRITE.three_write(0x22,0x52);
	  //call Sccb_OVWRITE.three_write(0x5e,0x53);
	  //call Sccb_OVWRITE.three_write(0x80,0x54);
	// call Sccb_OVWRITE.three_write(COM13_GAMMA|COM13_UVSAT,REG_COM13);
	  /* test pattern
	  call Sccb_OVWRITE.three_write(0x3A, 0x70);
	  call Sccb_OVWRITE.three_write(0xB5, 0x71);
	  */
	  //TOSH_uwait(20000);
	/*
	  j = (sizeof(init_array_qcif) / sizeof(init_array_qcif[0]));
	  for (i = 0; i < j; i++) {
	    call Sccb_OVWRITE.three_write(init_array_qcif[i][1], init_array_qcif[i][0]); // val, reg
	  }*/
	  global_stat.config = OV_CONFIG_YUV;
	  global_stat.color = COLOR_UYVY;
	}
	
	command void HplOV7670.config_rgb()
	{
		//call Sccb_OVWRITE.three_write(0x11,FACT); 	// RGB 565
	  call Sccb_OVWRITE.three_write(COM7_RGB | COM7_FMT_QVGA, REG_COM7); 	// RGB 565
	  call Sccb_OVWRITE.three_write(0,REG_RGB444); 	// RGB 565
	  call Sccb_OVWRITE.three_write(COM15_RGB565,REG_COM15); 	// RGB 565

	  //call Sccb_OVWRITE.three_write(0xb3,0x4f);
	  //call Sccb_OVWRITE.three_write(0xb3,0x50);
	  //call Sccb_OVWRITE.three_write(0,0x51);
	  //call Sccb_OVWRITE.three_write(0x3d,0x52);
	  //call Sccb_OVWRITE.three_write(0xa7,0x53);
	  //call Sccb_OVWRITE.three_write(0xe4,0x54);
	  //call Sccb_OVWRITE.three_write(COM13_GAMMA|COM13_UVSAT|0x2,REG_COM13);
	  /* test pattern
	  call Sccb_OVWRITE.three_write(0x3A, 0x70);
	  call Sccb_OVWRITE.three_write(0xB5, 0x71);
	  */
	  global_stat.config = OV_CONFIG_RGB;
	  global_stat.color = COLOR_RGB565;
	  //TOSH_uwait(1000);
	}

	command void HplOV7670.config_window(uint8_t img_size)
	{

	//SET MY OWN FORMAT	
	/*	uint8_t hstrt,hstop,vstrt,vstop;
		hstrt = WINDOW_HZERO + 0/2;
        	hstop = WINDOW_HZERO + (0 + 200)/2;
	        vstrt = WINDOW_VZERO + 0;
	        vstop = WINDOW_VZERO + 0 + 152;
	
	    call Sccb_OVWRITE.three_write(hstrt, 0x17); // HSTART
	    call Sccb_OVWRITE.three_write(hstop, 0x18); // HSTOP
	    call Sccb_OVWRITE.three_write(vstrt, 0x19); // VSTART
	    call Sccb_OVWRITE.three_write(vstop, 0x1A); // VSTOP
	    call Sccb_OVWRITE.three_write(0xB6, 0x32); // HREF	 
	*/


		if(img_size==SIZE_VGA){
	    call Sccb_OVWRITE.three_write(0x13, 0x17); // HSTART
	    call Sccb_OVWRITE.three_write(0x01, 0x18); // HSTOP
	    call Sccb_OVWRITE.three_write(0x02, 0x19); // VSTART
	    call Sccb_OVWRITE.three_write(0xfA, 0x1A); // VSTOP
	    call Sccb_OVWRITE.three_write(0xB6, 0x32); // HREF	 
	}
	else{
		/* QVGA settings in acquire and plotting QCIF*/
	    call Sccb_OVWRITE.three_write(0x13,REG_HSTART); // HSTART
	    call Sccb_OVWRITE.three_write(0x01, REG_HSTOP); // HSTOP
	    call Sccb_OVWRITE.three_write(0xb6, REG_VSTART); // VSTART
	    call Sccb_OVWRITE.three_write(0x7a,REG_VSTOP); // VSTOP
	    call Sccb_OVWRITE.three_write(0x0a, REG_VREF); // HREF
	   }

	}
	
	async command ov_stat_t *HplOV7670.get_config()
	{
		return &global_stat;
	}
}
