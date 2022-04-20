#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2022 gr-hornet author.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy
from gnuradio import gr
import pmt

class str_to_pdu(gr.basic_block):
    """
    This block accepts message as a tuple containing two strings where second string carries and text information that is going to be encoded into the PDU payload (cdr) 
    """
    def __init__(self):
        gr.basic_block.__init__(self,
            name="Message to PDU",
            in_sig=None,
            out_sig=None)

        self.message_port_register_in(pmt.intern('in'))
        self.message_port_register_out(pmt.intern('out'))
        self.set_msg_handler(pmt.intern('in'), self.handle_msg)
        self.counter = 0

        
    def handle_msg(self, msg):
        p_var = pmt.to_python(msg) # tuple with two elements (key, value) - data is in Value
        #print("Type of the message: ",type(p_var))
        #print("Type of the first element: ", type(p_var[0]))
        #print("Type of the second element: ", type(p_var[1]))
        s_value = p_var[1] + " " + str(self.counter) + "\n" # adding message number to be easier identified in the receiver
        #ascii_list = [int(ord(v)) for v in p_var[1]]
        ascii_list = [int(ord(v)) for v in s_value]        
        vector = pmt.init_u8vector(len(ascii_list), ascii_list)
        pdu = pmt.cons(pmt.PMT_NIL, vector)
        self.message_port_pub(pmt.intern('out'), pdu)
        self.counter+=1      
