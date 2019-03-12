#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Tue Mar 12 17:05:48 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import mysvl
import relative_paths  # embedded python module
import sys
import time


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.freq = freq = 2375e6
        self.udp_len = udp_len = 1472*16
        self.time_preamble = time_preamble =  [0.125000+0.000000j, 0.522104-0.148216j, -0.495528+0.114832j, -0.267916+0.091700j, 0.236544-0.138456j, -0.098500+0.473800j, 0.476480-0.225344j, -0.187516+0.035372j, 0.051776-0.353552j, -0.104936+0.059916j,  0.228684+0.117504j, -0.530912+0.560756j, 0.359128+0.015872j, -0.132852+0.632840j, -0.105164-0.368872j, 0.368272-0.032412j, 0.125000+0.750000j, 0.463968+0.457792j, 0.151476-0.430948j, 0.685052+0.238524j, 0.494428+0.119428j, -0.557540-0.050056j, 0.416348+0.017368j, 0.104256-0.568836j, -0.301776-0.353552j, 0.079812+0.451516j, 0.439152+0.528072j, 0.642060+0.178484j, -0.090096+0.465096j, -0.446492+0.305776j, -0.111440-0.093688j, -0.538848-0.320228j, 0.125000+0.000000j, -0.538848+0.320228j, -0.111440+0.093688j, -0.446492-0.305776j, -0.090096-0.465096j, 0.642060-0.178484j, 0.439152-0.528072j, 0.079812-0.451516j, -0.301776+0.353552j, 0.104256+0.568836j, 0.416348-0.017368j, -0.557540+0.050056j, 0.494428-0.119428j, 0.685052-0.238524j, 0.151476+0.430948j, 0.463968-0.457792j, 0.125000-0.750000j, 0.368272+0.032412j, -0.105164+0.368872j, -0.132852-0.632840j, 0.359128-0.015872j, -0.530912-0.560756j, 0.228684-0.117504j, -0.104936-0.059916j, 0.051776+0.353552j, -0.187516-0.035372j, 0.476480+0.225344j, -0.098500-0.473800j, 0.236544+0.138456j, -0.267916-0.091700j, -0.495528-0.114832j, 0.522104+0.148216j]
        self.samp_rate = samp_rate = 1700000
        self.preamble_len = preamble_len = 64
        self.padding = padding = 12
        self.packet_len = packet_len = 1024*4
        self.number_len = number_len = 6*4*8
        self.length = length = 96
        self.gain2 = gain2 = 0.7
        self.gain = gain = 0.7
        self.freq2 = freq2 = freq+5e6

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_sink_0_0 = uhd.usrp_sink(
        	",".join(("", "serial= 30C6272")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0_0.set_subdev_spec("A:B", 0)
        self.uhd_usrp_sink_0_0.set_time_unknown_pps(uhd.time_spec())
        self.uhd_usrp_sink_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0_0.set_center_freq(freq, 0)
        self.uhd_usrp_sink_0_0.set_normalized_gain(gain, 0)
        self.uhd_usrp_sink_0_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "serial=30C628B")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_subdev_spec("A:A", 0)
        self.uhd_usrp_sink_0.set_time_unknown_pps(uhd.time_spec())
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(freq2, 0)
        self.uhd_usrp_sink_0.set_normalized_gain(gain2, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        self.mysvl_svl_1 = mysvl.svl(gr.sizeof_gr_complex*1, 1, "./inputs/spectrum_maps/one_many_tx.txt", "./inputs/parameters/one_many_tx.txt")
        self.mysvl_stream_demux_0_0 = mysvl.stream_demux(gr.sizeof_gr_complex*1, (1,packet_len-2,1), False)
        self.mysvl_stream_demux_0 = mysvl.stream_demux(gr.sizeof_gr_complex*1, (1,packet_len-2,1), False)
        self.digital_ofdm_tx_0 = digital.ofdm_tx(
        	  fft_len=64, cp_len=16,
        	  packet_length_tag_key="length",
        	  bps_header=1,
        	  bps_payload=1,
        	  rolloff=0,
        	  debug_log=False,
        	  scramble_bits=False
        	 )
        self.digital_gfsk_mod_0 = digital.gfsk_mod(
        	samples_per_symbol=2,
        	sensitivity=1.0,
        	bt=0.35,
        	verbose=False,
        	log=False,
        )
        self.blocks_vector_source_x_1_0 = blocks.vector_source_b(range(1,65), True, 1, [])
        self.blocks_vector_source_x_0_0 = blocks.vector_source_c(time_preamble, True, 1, [])
        self.blocks_vector_source_x_0 = blocks.vector_source_c(time_preamble, True, 1, [])
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, length, "length")
        self.blocks_stream_mux_1_0 = blocks.stream_mux(gr.sizeof_gr_complex*1, (padding+1, packet_len-2,padding+1))
        self.blocks_stream_mux_1 = blocks.stream_mux(gr.sizeof_gr_complex*1, (padding+1, packet_len-2,padding+1))
        self.blocks_stream_mux_0_0 = blocks.stream_mux(gr.sizeof_gr_complex*1, (preamble_len, number_len, packet_len+2*padding))
        self.blocks_stream_mux_0 = blocks.stream_mux(gr.sizeof_gr_complex*1, (preamble_len, number_len,packet_len+2*padding))
        self.blocks_repeat_0_1 = blocks.repeat(gr.sizeof_gr_complex*1, padding+1)
        self.blocks_repeat_0_0_0 = blocks.repeat(gr.sizeof_gr_complex*1, padding+1)
        self.blocks_repeat_0_0 = blocks.repeat(gr.sizeof_gr_complex*1, padding+1)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_gr_complex*1, padding+1)
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_vcc((0.5, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((0.025, ))
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_char*1, "./inputs/Memory_and_Forgetting.mp3", True)
        self.blks2_packet_encoder_0 = grc_blks2.packet_mod_b(grc_blks2.packet_encoder(
        		samples_per_symbol=2,
        		bits_per_symbol=1,
        		preamble="",
        		access_code="",
        		pad_for_usrp=False,
        	),
        	payload_length=1,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blks2_packet_encoder_0, 0), (self.digital_gfsk_mod_0, 0))    
        self.connect((self.blocks_file_source_0_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.mysvl_svl_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.blocks_stream_mux_0, 1))    
        self.connect((self.blocks_repeat_0, 0), (self.blocks_stream_mux_1, 2))    
        self.connect((self.blocks_repeat_0_0, 0), (self.blocks_stream_mux_1, 0))    
        self.connect((self.blocks_repeat_0_0_0, 0), (self.blocks_stream_mux_1_0, 0))    
        self.connect((self.blocks_repeat_0_1, 0), (self.blocks_stream_mux_1_0, 2))    
        self.connect((self.blocks_stream_mux_0, 0), (self.uhd_usrp_sink_0_0, 0))    
        self.connect((self.blocks_stream_mux_0_0, 0), (self.uhd_usrp_sink_0, 0))    
        self.connect((self.blocks_stream_mux_1, 0), (self.blocks_stream_mux_0, 2))    
        self.connect((self.blocks_stream_mux_1_0, 0), (self.blocks_stream_mux_0_0, 2))    
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.digital_ofdm_tx_0, 0))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_stream_mux_0, 0))    
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.blocks_stream_mux_0_0, 0))    
        self.connect((self.blocks_vector_source_x_1_0, 0), (self.blks2_packet_encoder_0, 0))    
        self.connect((self.digital_gfsk_mod_0, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))    
        self.connect((self.digital_gfsk_mod_0, 0), (self.blocks_stream_mux_0_0, 1))    
        self.connect((self.digital_ofdm_tx_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.mysvl_stream_demux_0, 2), (self.blocks_repeat_0, 0))    
        self.connect((self.mysvl_stream_demux_0, 0), (self.blocks_repeat_0_0, 0))    
        self.connect((self.mysvl_stream_demux_0, 1), (self.blocks_stream_mux_1, 1))    
        self.connect((self.mysvl_stream_demux_0_0, 0), (self.blocks_repeat_0_0_0, 0))    
        self.connect((self.mysvl_stream_demux_0_0, 2), (self.blocks_repeat_0_1, 0))    
        self.connect((self.mysvl_stream_demux_0_0, 1), (self.blocks_stream_mux_1_0, 1))    
        self.connect((self.mysvl_svl_1, 0), (self.mysvl_stream_demux_0, 0))    
        self.connect((self.mysvl_svl_1, 1), (self.mysvl_stream_demux_0_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.set_freq2(self.freq+5e6)
        self.uhd_usrp_sink_0_0.set_center_freq(self.freq, 0)

    def get_udp_len(self):
        return self.udp_len

    def set_udp_len(self, udp_len):
        self.udp_len = udp_len

    def get_time_preamble(self):
        return self.time_preamble

    def set_time_preamble(self, time_preamble):
        self.time_preamble = time_preamble
        self.blocks_vector_source_x_0_0.set_data(self.time_preamble, [])
        self.blocks_vector_source_x_0.set_data(self.time_preamble, [])

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink_0_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0_0.set_bandwidth(self.samp_rate/2, 1)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

    def get_preamble_len(self):
        return self.preamble_len

    def set_preamble_len(self, preamble_len):
        self.preamble_len = preamble_len

    def get_padding(self):
        return self.padding

    def set_padding(self, padding):
        self.padding = padding

    def get_packet_len(self):
        return self.packet_len

    def set_packet_len(self, packet_len):
        self.packet_len = packet_len

    def get_number_len(self):
        return self.number_len

    def set_number_len(self, number_len):
        self.number_len = number_len

    def get_length(self):
        return self.length

    def set_length(self, length):
        self.length = length
        self.blocks_stream_to_tagged_stream_0.set_packet_len(self.length)
        self.blocks_stream_to_tagged_stream_0.set_packet_len_pmt(self.length)

    def get_gain2(self):
        return self.gain2

    def set_gain2(self, gain2):
        self.gain2 = gain2
        self.uhd_usrp_sink_0_0.set_normalized_gain(self.gain2, 1)
        	
        self.uhd_usrp_sink_0.set_normalized_gain(self.gain2, 0)
        	

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.uhd_usrp_sink_0_0.set_normalized_gain(self.gain, 0)
        	

    def get_freq2(self):
        return self.freq2

    def set_freq2(self, freq2):
        self.freq2 = freq2
        self.uhd_usrp_sink_0_0.set_center_freq(self.freq2, 1)
        self.uhd_usrp_sink_0.set_center_freq(self.freq2, 0)


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
