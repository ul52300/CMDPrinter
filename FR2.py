import PySimpleGUI as sg

TEXT_FONT_UNDERLINE = ('Times New Roman', 10, 'bold', 'underline')
TEXT_FONT = ('Times New Roman', 10, 'bold')

def main_window():
    sg.theme('Neutral Blue')
    
    layout = [
        # [
        #     sg.Text(
        #         'What pol?',
        #         size=(20,1),
        #         font=TEXT_FONT
        #     ),
        #     sg.Combo(
        #         values=['H','V','H+V'],
        #         key="-choose_pols-",
        #         default_value="",
        #         readonly=True,
        #         size=(15,1)
        #     )
        # ],
        [
            sg.Text(
                'AT+NRFFINALSTART',
                font=TEXT_FONT_UNDERLINE
            )
        ],        
        [
            sg.Text(
                'Band',
                size=(20,1),
                font=TEXT_FONT
            ),
            sg.Combo(
                values=['n257', 'n258', 'n260', 'n261'],
                key="-band-",
                default_value="",
                readonly=True,
                size=(15,1)
            ),
            sg.Text(
                key="-error_band-"
            )
        ],
        [
            sg.Text(
                'AT+MMTXSTART',
                font=TEXT_FONT_UNDERLINE
            )
        ],
        [
            sg.Text(
                'Plane',
                size=(20,1),
                font=TEXT_FONT
            ),
            sg.Combo(
                values=['A-Plane', 'B-Plane'],
                key="-plane-",
                default_value="",
                tooltip="0 = B-Plane\n1 = A-Plane",
                readonly=True,
                size=(15,1)
            ),
            sg.Text(
                key="-error_plane-"
            )
        ],
        [
            sg.Text(
                'Frequency (kHz)',
                size=(20,1),
                font=TEXT_FONT
            ),
            sg.Combo(
                values=['25875000', '27925000', '28000000', '38500000'],
                key="-frequency-",
                default_value="",
                tooltip="n257 = 28000000\nn258 = 25875000\nn260 = 38500000\nn261 = 27925000",
                readonly=True,
                size=(15,1)
            ),
            sg.Text(
                key="-error_frequency-"
            )
        ],
        [
            sg.Text(
                'Tx Power',
                size=(20,1),
                font=TEXT_FONT
            ),
            sg.Input(
                key="-txpwr-",
                tooltip="Enter the power in dBm",
                size=(15,1)
            ),
            sg.Text(
                key="-error_pwr-"
            )
        ],
        [
            sg.Text(
                'AT+NBEAMSET',
                font=TEXT_FONT_UNDERLINE
            )
        ],
        [
            sg.Text(
                'Wide or Narrow?',
                size=(20,1),
                font=TEXT_FONT
            ),
            sg.Combo(
                values=['Wide','Narrow'],
                key="-beam_type-",
                default_value="",
                tooltip="Beam ID only goes from:\nWide Beam = 0 to 2\nNarrow Beam = 0 to 6",
                readonly=True,
                size=(15,1)
            ),
            sg.Text(
                key="-error_beamtype-"
            )
        ],
        [
            sg.Text(
                'Beam ID (H)',
                size=(20,1),
                font=TEXT_FONT
            ),
            sg.Combo(
                values=['OFF']+list(range(0,7)),
                key="-beam_id_h-",
                default_value="",
                tooltip="Beam ID only goes from:\nWide Beam = 0 to 2\nNarrow Beam = 0 to 6",
                readonly=True,
                size=(15,1)
            ),
            sg.Text(
                key="-error_beamidh-"
            )
        ],
        [
            sg.Text(
                'Beam ID (V)',
                size=(20,1),
                font=TEXT_FONT
            ),
            sg.Combo(
                values=['OFF']+list(range(0,7)),
                key="-beam_id_v-",
                default_value="",
                tooltip="Beam ID only goes from:\nWide Beam = 0 to 2\nNarrow Beam = 0 to 6",
                readonly=True,
                size=(15,1)
            ),
            sg.Text(
                key="-error_beamidv-"
            )
        ],
        [sg.HorizontalSeparator()],
        [
            sg.Text(
                'BAND CMD',
                size=(20,1),
                font=TEXT_FONT
            ),
            sg.Input(
                key="-result_band_command-",
                font=TEXT_FONT
            )
        ],
        [
            sg.Text(
                'START CMD 1',
                size=(20,1),
                font=TEXT_FONT
            ),
            sg.Input(
                key="-result_start_command1-",
                font=TEXT_FONT
            )
        ],
        [
            sg.Text(
                'BEAM CMD 1',
                size=(20,1),
                font=TEXT_FONT
            ),
            sg.Input(
                key="-result_beam_command1-",
                font=TEXT_FONT
            )
        ],
        [
            sg.Text(
                'START CMD 2',
                size=(20,1),
                font=TEXT_FONT
            ),
            sg.Input(
                key="-result_start_command2-",
                font=TEXT_FONT
            )
        ],
        [
            sg.Text(
                'BEAM CMD 2',
                size=(20,1),
                font=TEXT_FONT
            ),
            sg.Input(
                key="-result_beam_command2-",
                font=TEXT_FONT
            )
        ],
        [
            sg.Button(
                'Give me the Goods'
            )
        ]
    ]
    return(sg.Window('FR2', layout,size=(500,445), resizable=False, location=(0,0), finalize=True))

def updateWindow(key, message):
    return(window[str(key)].update(message))

def updateError(band, plane, frequency, pwr, beamtype, beamidh, beamidv):
        updateWindow("-error_band-", "Please Enter Band!") if band == "" else updateWindow("-error_band-", "")
        updateWindow("-error_plane-", "Please Enter Plane!") if plane == "" else updateWindow("-error_plane-", "")
        updateWindow("-error_frequency-", "Please Enter Frequency!") if frequency == "" else updateWindow("-error_frequency-", "")
        updateWindow("-error_pwr-", "Please Enter Power!")  if pwr == "" else updateWindow("-error_pwr-", "")
        updateWindow("-error_beamtype-", "Please Enter Beam Type!") if beamtype == "" else updateWindow("-error_beamtype-", "")
        updateWindow("-error_beamidh-", "Please Enter Hpol Beam ID!") if beamidh == "" else updateWindow("-error_beamidh-", "")
        updateWindow("-error_beamidv-", "Please Enter Vpol Beam ID!") if beamidv == "" else updateWindow("-error_beamidv-", "")
        

if __name__ == "__main__":
    window1 = main_window()
    while True:
        window, event, values = sg.read_all_windows()
        
        if event == sg.WIN_CLOSED:
            window.close()
            if window == window1:
                break
        elif event == "Give me the Goods" and all(var != "" for var in [values["-band-"], values["-plane-"], values["-frequency-"], values["-txpwr-"], values["-beam_type-"], str(values["-beam_id_h-"]), str(values["-beam_id_v-"])]):
            updateError(values["-band-"], values["-plane-"], values["-frequency-"], values["-txpwr-"], values["-beam_type-"], values["-beam_id_h-"], values["-beam_id_v-"])
            #pol = values["-choose_pols-"]       # H or V or H+V pol.
            band = values["-band-"]             # Band
            plane = values["-plane-"]           # P0 - Plane
            frequency = values["-frequency-"]   # P1 - Frequency
            bandwidth = "14"                    # P2 - Bandwidth | 14 = 100 MHz
            scs = 3                             # P3 - Subcarrier Spacing | 3 = 120 kHz
            rb_size1 = "66"                     # P4 - RB Number first command | 66 RBs
            rb_offset1 = "0"                    # P5 - RB Start first command | RB Start at 0
            rb_size2 = "0"                      # P4 - RB Number second command | 0 RBs
            rb_offset2 = "648"                  # P5 - RB Start second command | RB Start at 648(?)
            modulation = "2"                    # P6 - Modulation | 2 = QPSK
            fr2_type = "1"                      # P7 - FR2 Type | 1 = CP-OFDM
            txpwr = values["-txpwr-"]           # P8 - Transmission power
            trxtype = "1"                       # Tx or Rx (1 or 0)
            beam_type = values["-beam_type-"]   # Beam type (Wide or Narrow)
            hpol = str(values["-beam_id_h-"])   # Beam ID Hpol
            vpol = str(values["-beam_id_v-"])   # Beam ID Vpol
            
            match plane:
                case "A-Plane": plane = "1"
                case "B-Plane": plane = "0"
            
            match band:
                case "n257": band = "257"
                case "n258": band = "258"                
                case "n260": band = "260"                
                case "n261": band = "261"
            
            match beam_type:
                case "Wide":
                    beam_idh = ("{}FE" if hpol == "OFF" else "{}0{}").format(int(plane) + 1, hpol)
                    beam_idv = ("{}FE" if vpol == "OFF" else "{}0{}").format(int(plane) + 1, vpol)
                case "Narrow":
                    beam_idh = ("{}FE" if hpol == "OFF" else "{}8{}").format(int(plane) + 1, hpol)
                    beam_idv = ("{}FE" if vpol == "OFF" else "{}8{}").format(int(plane) + 1, vpol)
                
            # if pol != "H+V":
            #     start_command = "{},{},{},{},{},{},{},{},{}".format(plane,frequency,bandwidth,scs,rb_size,rb_offset,modulation,fr2_type,txpwr)
            #     beam_cmd = "{},{},{}".format(trxtype, (str(int(plane)+1)+beam_type+hpol), (str(int(plane)+1)+beam_type+vpol))
                
            #     window["-result_band_command-"].update("AT+NRFFINALSTART={}".format(band))                    
            #     window["-result_start_command1-"].update("AT+MMTXSTART={}".format(start_command))
            #     window["-result_beam_command1-"].update("AT+NBEAMSET={}".format(beam_cmd))                  
            #     window["-result_start_command2-"].update("OFF")
            #     window["-result_beam_command2-"].update("OFF")                
            # else:
            start_command1 = "{},{},{},{},{},{},{},{},{}".format(plane,frequency,bandwidth,scs,rb_size1,rb_offset1,modulation,fr2_type,txpwr)
            beam_cmd1 = "{},{},{}".format(trxtype, beam_idh, beam_idv)
            start_command2 = "{},{},{},{},{},{},{},{},{}".format(plane,frequency,bandwidth,scs,rb_size2,rb_offset2,modulation,fr2_type,txpwr)
            beam_cmd2 = "{},{},{}".format(trxtype, beam_idh, beam_idv)
            
            window["-result_band_command-"].update("AT+NRFFINALSTART={}".format(band))                    
            window["-result_start_command1-"].update("AT+MMTXSTART={}".format(start_command1))
            window["-result_beam_command1-"].update("AT+NBEAMSET={}".format(beam_cmd1))                               
            window["-result_start_command2-"].update("AT+MMTXSTART={}".format(start_command2))
            window["-result_beam_command2-"].update("AT+NBEAMSET={}".format(beam_cmd2))
        elif event == "Give me the Goods" and any(var == "" for var in [values["-band-"], values["-plane-"], values["-frequency-"], values["-txpwr-"], values["-beam_type-"], str(values["-beam_id_h-"]), str(values["-beam_id_v-"])]):
            updateError(values["-band-"], values["-plane-"], values["-frequency-"], values["-txpwr-"], values["-beam_type-"], values["-beam_id_h-"], values["-beam_id_v-"])