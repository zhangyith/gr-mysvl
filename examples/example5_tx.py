#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Example5 Tx
# Generated: Tue Sep 18 18:09:42 2018
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import mysvl
import relative_paths  # embedded python module
import sip
import sys
from gnuradio import qtgui


class example5_tx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Example5 Tx")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Example5 Tx")
        qtgui.util.check_set_qss()
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

        self.settings = Qt.QSettings("GNU Radio", "example5_tx")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.time_preamble = time_preamble =  [0.125000+0.000000j, 0.522104-0.148216j, -0.495528+0.114832j, -0.267916+0.091700j, 0.236544-0.138456j, -0.098500+0.473800j, 0.476480-0.225344j, -0.187516+0.035372j, 0.051776-0.353552j, -0.104936+0.059916j,  0.228684+0.117504j, -0.530912+0.560756j, 0.359128+0.015872j, -0.132852+0.632840j, -0.105164-0.368872j, 0.368272-0.032412j, 0.125000+0.750000j, 0.463968+0.457792j, 0.151476-0.430948j, 0.685052+0.238524j, 0.494428+0.119428j, -0.557540-0.050056j, 0.416348+0.017368j, 0.104256-0.568836j, -0.301776-0.353552j, 0.079812+0.451516j, 0.439152+0.528072j, 0.642060+0.178484j, -0.090096+0.465096j, -0.446492+0.305776j, -0.111440-0.093688j, -0.538848-0.320228j, 0.125000+0.000000j, -0.538848+0.320228j, -0.111440+0.093688j, -0.446492-0.305776j, -0.090096-0.465096j, 0.642060-0.178484j, 0.439152-0.528072j, 0.079812-0.451516j, -0.301776+0.353552j, 0.104256+0.568836j, 0.416348-0.017368j, -0.557540+0.050056j, 0.494428-0.119428j, 0.685052-0.238524j, 0.151476+0.430948j, 0.463968-0.457792j, 0.125000-0.750000j, 0.368272+0.032412j, -0.105164+0.368872j, -0.132852-0.632840j, 0.359128-0.015872j, -0.530912-0.560756j, 0.228684-0.117504j, -0.104936-0.059916j, 0.051776+0.353552j, -0.187516-0.035372j, 0.476480+0.225344j, -0.098500-0.473800j, 0.236544+0.138456j, -0.267916-0.091700j, -0.495528-0.114832j, 0.522104+0.148216j]
        self.time_offset = time_offset = 1
        self.samp_rate = samp_rate = 500000
        self.preamble_len = preamble_len = 64
        self.packet_len = packet_len = 1024
        self.noise = noise = 0
        self.length = length = 96
        self.freq_offset = freq_offset = 0

        ##################################################
        # Blocks
        ##################################################
        self._time_offset_range = Range(0.999, 1.001, 0.00001, 1, 200)
        self._time_offset_win = RangeWidget(self._time_offset_range, self.set_time_offset, 'Time offset', "counter_slider", float)
        self.top_grid_layout.addWidget(self._time_offset_win, 2, 0, 1, 2)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(2,3)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(0,2)]
        self._noise_range = Range(0, 0.2, 0.001, 0, 200)
        self._noise_win = RangeWidget(self._noise_range, self.set_noise, 'Noise', "counter_slider", float)
        self.top_grid_layout.addWidget(self._noise_win, 0, 0, 1, 2)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(0,1)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(0,2)]
        self._freq_offset_range = Range(0, 0.02, 0.0001, 0, 200)
        self._freq_offset_win = RangeWidget(self._freq_offset_range, self.set_freq_offset, 'Freq offset', "counter_slider", float)
        self.top_grid_layout.addWidget(self._freq_offset_win, 1, 0, 1, 2)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(1,2)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(0,2)]
        self.qtgui_freq_sink_x_0_0_0_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Real Spectrum", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_0_0.set_y_axis(-80, -20)
        self.qtgui_freq_sink_x_0_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0_0_0.set_plot_pos_half(not True)

        labels = ['MySVL Signal', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_0_win, 3, 0, 1, 2)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(3,4)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(0,2)]
        self.mysvl_svl_1 = mysvl.svl(gr.sizeof_gr_complex*1, 1, './inputs/spectrum_maps/example1b_tx.txt', './inputs/parameters/example1a-c_tx.txt')
        self.low_pass_filter_0_0 = filter.interp_fir_filter_ccf(2, firdes.low_pass(
        	1, samp_rate, samp_rate/4-samp_rate/32, samp_rate/32, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.interp_fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, samp_rate/2-samp_rate/32, samp_rate/32, firdes.WIN_HAMMING, 6.76))
        self.digital_ofdm_tx_0 = digital.ofdm_tx(
        	  fft_len=64, cp_len=16,
        	  packet_length_tag_key='length',
        	  bps_header=1,
        	  bps_payload=2,
        	  rolloff=0,
        	  debug_log=False,
        	  scramble_bits=False
        	 )
        self.digital_gmsk_mod_0 = digital.gmsk_mod(
        	samples_per_symbol=2,
        	bt=0.35,
        	verbose=False,
        	log=False,
        )
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=noise,
        	frequency_offset=freq_offset,
        	epsilon=time_offset,
        	taps=(1+1j, ),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_vector_source_x_0 = blocks.vector_source_c(time_preamble, True, 1, [])
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_gr_complex*1, '127.0.0.1', 4000, 1472*32, True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, length, "length")
        self.blocks_stream_mux_0 = blocks.stream_mux(gr.sizeof_gr_complex*1, (preamble_len, packet_len))
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_vcc((0.1, ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vcc((2.0/4, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((0.05, ))
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_char*1, './inputs/Memory_and_Forgetting.mp3', True)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, './inputs/Memory_and_Forgetting.mp3', True)
        self.blks2_packet_encoder_1 = grc_blks2.packet_mod_b(grc_blks2.packet_encoder(
        		samples_per_symbol=2,
        		bits_per_symbol=1,
        		preamble='',
        		access_code='',
        		pad_for_usrp=False,
        	),
        	payload_length=0,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blks2_packet_encoder_1, 0), (self.digital_gmsk_mod_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.blocks_file_source_0_0, 0), (self.blks2_packet_encoder_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.blocks_udp_sink_0, 0))
        self.connect((self.blocks_stream_mux_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.digital_ofdm_tx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.channels_channel_model_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_stream_mux_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.blocks_multiply_const_vxx_0_1, 0))
        self.connect((self.channels_channel_model_0, 0), (self.qtgui_freq_sink_x_0_0_0_0, 0))
        self.connect((self.digital_gmsk_mod_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.digital_ofdm_tx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.mysvl_svl_1, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.mysvl_svl_1, 1))
        self.connect((self.mysvl_svl_1, 0), (self.blocks_stream_mux_0, 1))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "example5_tx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_time_preamble(self):
        return self.time_preamble

    def set_time_preamble(self, time_preamble):
        self.time_preamble = time_preamble
        self.blocks_vector_source_x_0.set_data(self.time_preamble, [])

    def get_time_offset(self):
        return self.time_offset

    def set_time_offset(self, time_offset):
        self.time_offset = time_offset
        self.channels_channel_model_0.set_timing_offset(self.time_offset)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0_0_0_0.set_frequency_range(0, self.samp_rate)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.samp_rate/4-self.samp_rate/32, self.samp_rate/32, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.samp_rate/2-self.samp_rate/32, self.samp_rate/32, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_preamble_len(self):
        return self.preamble_len

    def set_preamble_len(self, preamble_len):
        self.preamble_len = preamble_len

    def get_packet_len(self):
        return self.packet_len

    def set_packet_len(self, packet_len):
        self.packet_len = packet_len

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self.channels_channel_model_0.set_noise_voltage(self.noise)

    def get_length(self):
        return self.length

    def set_length(self, length):
        self.length = length
        self.blocks_stream_to_tagged_stream_0.set_packet_len(self.length)
        self.blocks_stream_to_tagged_stream_0.set_packet_len_pmt(self.length)

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset
        self.channels_channel_model_0.set_frequency_offset(self.freq_offset)


def main(top_block_cls=example5_tx, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
