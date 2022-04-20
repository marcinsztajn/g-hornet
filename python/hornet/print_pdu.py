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

class print_pdu(gr.basic_block):
    """
    Prints the encoded payload as a string
    """
    def __init__(self, mode='word'):
        gr.basic_block.__init__(self,
            name="Print PDU",
            in_sig=None,
            out_sig=None)

        self.mode = mode
        self.message_port_register_in(pmt.intern('in'))
        self.set_msg_handler(pmt.intern('in'), self.handle_msg)

    def handle_msg(self, msg):
        print("*** PRINT MESSAGE BLOCK ***")
        if self.mode == 'word':
            if pmt.is_pair(msg):
                if pmt.is_u8vector(pmt.cdr(msg)):
                    python_var = pmt.to_python(pmt.cdr(msg))
                    print("".join(chr(v) for v in python_var))
                else: 
                    #print("CDR is not u8vector")
                    #print("It's ",type(pmt.to_python(pmt.cdr(msg)))) - numpy array
                    print('In CAR: ', pmt.to_python(pmt.car(msg))) 
                    print('In CDR: ', pmt.to_python(pmt.cdr(msg)))
            else:
                print("Message is not a pair!")
        elif self.mode == 'number':
            python_var = pmt.to_python(pmt.cdr(msg))
            print(python_var)
        elif self.mode == 'binary':
            python_var = pmt.to_python(pmt.cdr(msg))
            print(format(python_var[0], '08b'))

        
        
