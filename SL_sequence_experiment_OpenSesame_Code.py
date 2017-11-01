Appendix X: OpenSesame Script
---
API: 2
OpenSesame: 3.1.7
Platform: nt
---
set width 1280
set uniform_coordinates no
set title "Runtime for Android template"
set synth_backend droid
set subject_parity even
set subject_nr 0
set start experiment
set sound_sample_size -16
set sound_freq 48000
set sound_channels 2
set sound_buf_size 1024
set sampler_backend legacy
set round_decimals 2
set mouse_backend droid
set keyboard_backend droid
set height 800
set fullscreen no
set form_clicks no
set foreground "#000000"
set font_underline no
set font_size 32
set font_italic no
set font_family mono
set font_bold no
set experiment_path "C:\\Users\\russe\\Dropbox"
set disable_garbage_collection yes
set description "A template containing a practice and an experimental phase"
set coordinates relative
set compensation 0
set color_backend legacy
set clock_backend legacy
set canvas_backend droid
set bidi no
set background "#ffffff"

define form_text_input Age
	set timeout infinite
	set spacing 10
	set rows "1;1;6"
	set only_render no
	set margins "50;50;50;50"
	set form_var age
	set form_title 2
	__form_question__
	How old are you?
	(Press Enter to confirm your answer)
	__end__
	set description "A simple text input form"
	set cols 1
	set button_text ok
	set _theme gray
	widget 0 0 1 1 label text="[form_title]"
	widget 0 1 1 1 label center=no text="[form_question]"
	widget 0 2 1 1 text_input focus=yes return_accepts=yes stub="" var="[form_var]"


define form_multiple_choice Consent
	set timeout infinite
	set spacing 10
	set question ""
	set options "I confirm that my participation has been explained and consent to taking part in the experiment"
	set margins "50;50;50;50"
	set form_var consent
	set form_title 3
	set description "A simple multiple choice item"
	set button_text Ok
	set allow_multiple no
	set advance_immediately yes
	set _theme gray

define sketchpad Instructions
	set duration mouseclick
	set description "Displays stimuli"
	draw textline center=1 color="#000000" font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=always text="Thank you for participating in this experiment." x=32 y=-352 z_index=0
	draw rect color="#ff0000" fill=1 h=200 penwidth=1 show_if=always w=200 x=0 y=-320 z_index=0
	draw rect color="#0000ff" fill=1 h=200 penwidth=1 show_if=always w=200 x=-224 y=-320 z_index=0
	draw rect color="#00ff00" fill=1 h=200 penwidth=1 show_if=always w=200 x=-224 y=-96 z_index=0
	draw rect color="#ffff00" fill=1 h=200 penwidth=1 show_if=always w=200 x=0 y=-96 z_index=0
	draw textline center=1 color="#000000" font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=always text="A star will flash in one of the coloured squares<br /><br />Your task is to tap the rectangle where you saw the star using the index finger of your right hand<br /><br />Try to do this as quickly as possible" x=0 y=224 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if=always x=-128 y=-224 z_index=-1

define loop Prac_block
	set source_file ""
	set source table
	set skip 0
	set repeat 2
	set order random
	set offset no
	set item Prac_sequence
	set description "Repeatedly runs another item"
	set cycles 8
	set continuous no
	set column_order "loc_1;loc_2;loc_3;loc_4;correct_response"
	set break_if_on_first yes
	set break_if never
	setcycle 0 loc 1
	setcycle 1 loc 2
	setcycle 2 loc 3
	setcycle 3 loc 4
	setcycle 4 loc 5
	setcycle 5 loc 6
	setcycle 6 loc 7
	setcycle 7 loc 8
	run trial_sequence_3

define form_multiple_choice Sex
	set timeout infinite
	set spacing 10
	set question "Are you male or female?"
	__options__
	Male
	Female
	Prefer not to say
	__end__
	set margins "50;50;50;50"
	set form_var sex
	set form_title 1
	set description "A simple multiple choice item"
	set button_text Ok
	set allow_multiple no
	set advance_immediately no
	set _theme gray

define loop block_1
	set source_file ""
	set source table
	set skip 0
	set repeat 1
	set order sequential
	set offset no
	set item trial_sequence
	set description "Repeatedly runs another item"
	set cycles 37
	set continuous no
	set column_order "freq; key; loc; tp"
	set break_if_on_first yes
	set break_if never
	setcycle 0 block 1
	setcycle 0 freq 2
	setcycle 0 key 71
	setcycle 0 loc 1
	setcycle 0 tp 0.33
	setcycle 1 block 1
	setcycle 1 freq 3
	setcycle 1 key 15
	setcycle 1 loc 5
	setcycle 1 tp 1
	setcycle 2 block 1
	setcycle 2 freq 3
	setcycle 2 key 54
	setcycle 2 loc 4
	setcycle 2 tp 0.6
	setcycle 3 block 1
	setcycle 3 freq 3
	setcycle 3 key 43
	setcycle 3 loc 3
	setcycle 3 tp 0.33
	setcycle 4 block 1
	setcycle 4 freq 1
	setcycle 4 key 36
	setcycle 4 loc 6
	setcycle 4 tp 0.2
	setcycle 5 block 1
	setcycle 5 freq 1
	setcycle 5 key 62
	setcycle 5 loc 2
	setcycle 5 tp 1
	setcycle 6 block 1
	setcycle 6 freq 1
	setcycle 6 key 28
	setcycle 6 loc 8
	setcycle 6 tp 0.2
	setcycle 7 block 1
	setcycle 7 freq 1
	setcycle 7 key 87
	setcycle 7 loc 7
	setcycle 7 tp 0.33
	setcycle 8 block 1
	setcycle 8 freq 2
	setcycle 8 key 71
	setcycle 8 loc 1
	setcycle 8 tp 0.33
	setcycle 9 block 1
	setcycle 9 freq 3
	setcycle 9 key 15
	setcycle 9 loc 5
	setcycle 9 tp 1
	setcycle 10 block 1
	setcycle 10 freq 1
	setcycle 10 key 58
	setcycle 10 loc 8
	setcycle 10 tp 0.2
	setcycle 11 block 1
	setcycle 11 freq 2
	setcycle 11 key 82
	setcycle 11 loc 2
	setcycle 11 tp 0.66
	setcycle 12 block 1
	setcycle 12 freq 2
	setcycle 12 key 24
	setcycle 12 loc 4
	setcycle 12 tp 0.4
	setcycle 13 block 1
	setcycle 13 freq 3
	setcycle 13 key 43
	setcycle 13 loc 3
	setcycle 13 tp 0.33
	setcycle 14 block 1
	setcycle 14 freq 1
	setcycle 14 key 31
	setcycle 14 loc 1
	setcycle 14 tp 0.2
	setcycle 15 block 1
	setcycle 15 freq 3
	setcycle 15 key 15
	setcycle 15 loc 5
	setcycle 15 tp 1
	setcycle 16 block 1
	setcycle 16 freq 3
	setcycle 16 key 54
	setcycle 16 loc 4
	setcycle 16 tp 0.6
	setcycle 17 block 1
	setcycle 17 freq 3
	setcycle 17 key 43
	setcycle 17 loc 3
	setcycle 17 tp 0.33
	setcycle 18 block 1
	setcycle 18 freq 1
	setcycle 18 key 37
	setcycle 18 loc 7
	setcycle 18 tp 0.2
	setcycle 19 block 1
	setcycle 19 freq 2
	setcycle 19 key 74
	setcycle 19 loc 4
	setcycle 19 tp 0.33
	setcycle 20 block 1
	setcycle 20 freq 2
	setcycle 20 key 47
	setcycle 20 loc 7
	setcycle 20 tp 0.22
	setcycle 21 block 1
	setcycle 21 freq 1
	setcycle 21 key 78
	setcycle 21 loc 8
	setcycle 21 tp 0.16
	setcycle 22 block 1
	setcycle 22 freq 2
	setcycle 22 key 82
	setcycle 22 loc 2
	setcycle 22 tp 0.66
	setcycle 23 block 1
	setcycle 23 freq 2
	setcycle 23 key 24
	setcycle 23 loc 4
	setcycle 23 tp 0.4
	setcycle 24 block 1
	setcycle 24 freq 1
	setcycle 24 key 45
	setcycle 24 loc 5
	setcycle 24 tp 0.11
	setcycle 25 block 1
	setcycle 25 freq 3
	setcycle 25 key 54
	setcycle 25 loc 4
	setcycle 25 tp 0.6
	setcycle 26 block 1
	setcycle 26 freq 2
	setcycle 26 key 47
	setcycle 26 loc 7
	setcycle 26 tp 0.22
	setcycle 27 block 1
	setcycle 27 freq 1
	setcycle 27 key 73
	setcycle 27 loc 3
	setcycle 27 tp 0.16
	setcycle 28 block 1
	setcycle 28 freq 1
	setcycle 28 key 34
	setcycle 28 loc 4
	setcycle 28 tp 0.2
	setcycle 29 block 1
	setcycle 29 freq 2
	setcycle 29 key 42
	setcycle 29 loc 2
	setcycle 29 tp 0.22
	setcycle 30 block 1
	setcycle 30 freq 1
	setcycle 30 key 23
	setcycle 30 loc 3
	setcycle 30 tp 0.2
	setcycle 31 block 1
	setcycle 31 freq 1
	setcycle 31 key 35
	setcycle 31 loc 5
	setcycle 31 tp 0.2
	setcycle 32 block 1
	setcycle 32 freq 1
	setcycle 32 key 57
	setcycle 32 loc 7
	setcycle 32 tp 0.2
	setcycle 33 block 1
	setcycle 33 freq 2
	setcycle 33 key 74
	setcycle 33 loc 4
	setcycle 33 tp 0.33
	setcycle 34 block 1
	setcycle 34 freq 1
	setcycle 34 key 44
	setcycle 34 loc 4
	setcycle 34 tp 0.11
	setcycle 35 block 1
	setcycle 35 freq 2
	setcycle 35 key 42
	setcycle 35 loc 2
	setcycle 35 tp 0.22
	setcycle 36 block 1
	setcycle 36 freq 1
	setcycle 36 key 27
	setcycle 36 loc 7
	setcycle 36 tp 0.2
	run trial_sequence_1

define loop block_2
	set source_file ""
	set source table
	set skip 0
	set repeat 1
	set order sequential
	set offset no
	set item trial_sequence
	set description "Repeatedly runs another item"
	set cycles 37
	set continuous no
	set column_order "loc_1;loc_2;loc_3;loc_4;correct_response;loc_5;loc_6;loc_8;loc_7"
	set break_if_on_first yes
	set break_if never
	setcycle 0 block 2
	setcycle 0 freq 2
	setcycle 0 key 71
	setcycle 0 loc 1
	setcycle 0 tp 0.33
	setcycle 1 block 2
	setcycle 1 freq 3
	setcycle 1 key 15
	setcycle 1 loc 5
	setcycle 1 tp 1
	setcycle 2 block 2
	setcycle 2 freq 3
	setcycle 2 key 54
	setcycle 2 loc 4
	setcycle 2 tp 0.6
	setcycle 3 block 2
	setcycle 3 freq 3
	setcycle 3 key 43
	setcycle 3 loc 3
	setcycle 3 tp 0.33
	setcycle 4 block 2
	setcycle 4 freq 1
	setcycle 4 key 36
	setcycle 4 loc 6
	setcycle 4 tp 0.2
	setcycle 5 block 2
	setcycle 5 freq 1
	setcycle 5 key 62
	setcycle 5 loc 2
	setcycle 5 tp 1
	setcycle 6 block 2
	setcycle 6 freq 1
	setcycle 6 key 28
	setcycle 6 loc 8
	setcycle 6 tp 0.2
	setcycle 7 block 2
	setcycle 7 freq 1
	setcycle 7 key 87
	setcycle 7 loc 7
	setcycle 7 tp 0.33
	setcycle 8 block 2
	setcycle 8 freq 2
	setcycle 8 key 71
	setcycle 8 loc 1
	setcycle 8 tp 0.33
	setcycle 9 block 2
	setcycle 9 freq 3
	setcycle 9 key 15
	setcycle 9 loc 5
	setcycle 9 tp 1
	setcycle 10 block 2
	setcycle 10 freq 1
	setcycle 10 key 58
	setcycle 10 loc 8
	setcycle 10 tp 0.2
	setcycle 11 block 2
	setcycle 11 freq 2
	setcycle 11 key 82
	setcycle 11 loc 2
	setcycle 11 tp 0.66
	setcycle 12 block 2
	setcycle 12 freq 2
	setcycle 12 key 24
	setcycle 12 loc 4
	setcycle 12 tp 0.4
	setcycle 13 block 2
	setcycle 13 freq 3
	setcycle 13 key 43
	setcycle 13 loc 3
	setcycle 13 tp 0.33
	setcycle 14 block 2
	setcycle 14 freq 1
	setcycle 14 key 31
	setcycle 14 loc 1
	setcycle 14 tp 0.2
	setcycle 15 block 2
	setcycle 15 freq 3
	setcycle 15 key 15
	setcycle 15 loc 5
	setcycle 15 tp 1
	setcycle 16 block 2
	setcycle 16 freq 3
	setcycle 16 key 54
	setcycle 16 loc 4
	setcycle 16 tp 0.6
	setcycle 17 block 2
	setcycle 17 freq 3
	setcycle 17 key 43
	setcycle 17 loc 3
	setcycle 17 tp 0.33
	setcycle 18 block 2
	setcycle 18 freq 1
	setcycle 18 key 37
	setcycle 18 loc 7
	setcycle 18 tp 0.2
	setcycle 19 block 2
	setcycle 19 freq 2
	setcycle 19 key 74
	setcycle 19 loc 4
	setcycle 19 tp 0.33
	setcycle 20 block 2
	setcycle 20 freq 2
	setcycle 20 key 47
	setcycle 20 loc 7
	setcycle 20 tp 0.22
	setcycle 21 block 2
	setcycle 21 freq 1
	setcycle 21 key 78
	setcycle 21 loc 8
	setcycle 21 tp 0.16
	setcycle 22 block 2
	setcycle 22 freq 2
	setcycle 22 key 82
	setcycle 22 loc 2
	setcycle 22 tp 0.66
	setcycle 23 block 2
	setcycle 23 freq 2
	setcycle 23 key 24
	setcycle 23 loc 4
	setcycle 23 tp 0.4
	setcycle 24 block 2
	setcycle 24 freq 1
	setcycle 24 key 45
	setcycle 24 loc 5
	setcycle 24 tp 0.11
	setcycle 25 block 2
	setcycle 25 freq 3
	setcycle 25 key 54
	setcycle 25 loc 4
	setcycle 25 tp 0.6
	setcycle 26 block 2
	setcycle 26 freq 2
	setcycle 26 key 47
	setcycle 26 loc 7
	setcycle 26 tp 0.22
	setcycle 27 block 2
	setcycle 27 freq 1
	setcycle 27 key 73
	setcycle 27 loc 3
	setcycle 27 tp 0.16
	setcycle 28 block 2
	setcycle 28 freq 1
	setcycle 28 key 34
	setcycle 28 loc 4
	setcycle 28 tp 0.2
	setcycle 29 block 2
	setcycle 29 freq 2
	setcycle 29 key 42
	setcycle 29 loc 2
	setcycle 29 tp 0.22
	setcycle 30 block 2
	setcycle 30 freq 1
	setcycle 30 key 23
	setcycle 30 loc 3
	setcycle 30 tp 0.2
	setcycle 31 block 2
	setcycle 31 freq 1
	setcycle 31 key 35
	setcycle 31 loc 5
	setcycle 31 tp 0.2
	setcycle 32 block 2
	setcycle 32 freq 1
	setcycle 32 key 57
	setcycle 32 loc 7
	setcycle 32 tp 0.2
	setcycle 33 block 2
	setcycle 33 freq 2
	setcycle 33 key 74
	setcycle 33 loc 4
	setcycle 33 tp 0.33
	setcycle 34 block 2
	setcycle 34 freq 1
	setcycle 34 key 44
	setcycle 34 loc 4
	setcycle 34 tp 0.11
	setcycle 35 block 2
	setcycle 35 freq 2
	setcycle 35 key 42
	setcycle 35 loc 2
	setcycle 35 tp 0.22
	setcycle 36 block 2
	setcycle 36 freq 1
	setcycle 36 key 27
	setcycle 36 loc 7
	setcycle 36 tp 0.2
	run trial_sequence_4

define loop block_3
	set source_file ""
	set source table
	set skip 0
	set repeat 1
	set order sequential
	set offset no
	set item trial_sequence
	set description "Repeatedly runs another item"
	set cycles 37
	set continuous no
	set column_order "loc_1;loc_2;loc_3;loc_4;correct_response;loc_5;loc_6;loc_8;loc_7"
	set break_if_on_first yes
	set break_if never
	setcycle 0 block 3
	setcycle 0 freq 2
	setcycle 0 key 71
	setcycle 0 loc 1
	setcycle 0 tp 0.33
	setcycle 1 block 3
	setcycle 1 freq 3
	setcycle 1 key 15
	setcycle 1 loc 5
	setcycle 1 tp 1
	setcycle 2 block 3
	setcycle 2 freq 3
	setcycle 2 key 54
	setcycle 2 loc 4
	setcycle 2 tp 0.6
	setcycle 3 block 3
	setcycle 3 freq 3
	setcycle 3 key 43
	setcycle 3 loc 3
	setcycle 3 tp 0.33
	setcycle 4 block 3
	setcycle 4 freq 1
	setcycle 4 key 36
	setcycle 4 loc 6
	setcycle 4 tp 0.2
	setcycle 5 block 3
	setcycle 5 freq 1
	setcycle 5 key 62
	setcycle 5 loc 2
	setcycle 5 tp 1
	setcycle 6 block 3
	setcycle 6 freq 1
	setcycle 6 key 28
	setcycle 6 loc 8
	setcycle 6 tp 0.2
	setcycle 7 block 3
	setcycle 7 freq 1
	setcycle 7 key 87
	setcycle 7 loc 7
	setcycle 7 tp 0.33
	setcycle 8 block 3
	setcycle 8 freq 2
	setcycle 8 key 71
	setcycle 8 loc 1
	setcycle 8 tp 0.33
	setcycle 9 block 3
	setcycle 9 freq 3
	setcycle 9 key 15
	setcycle 9 loc 5
	setcycle 9 tp 1
	setcycle 10 block 3
	setcycle 10 freq 1
	setcycle 10 key 58
	setcycle 10 loc 8
	setcycle 10 tp 0.2
	setcycle 11 block 3
	setcycle 11 freq 2
	setcycle 11 key 82
	setcycle 11 loc 2
	setcycle 11 tp 0.66
	setcycle 12 block 3
	setcycle 12 freq 2
	setcycle 12 key 24
	setcycle 12 loc 4
	setcycle 12 tp 0.4
	setcycle 13 block 3
	setcycle 13 freq 3
	setcycle 13 key 43
	setcycle 13 loc 3
	setcycle 13 tp 0.33
	setcycle 14 block 3
	setcycle 14 freq 1
	setcycle 14 key 31
	setcycle 14 loc 1
	setcycle 14 tp 0.2
	setcycle 15 block 3
	setcycle 15 freq 3
	setcycle 15 key 15
	setcycle 15 loc 5
	setcycle 15 tp 1
	setcycle 16 block 3
	setcycle 16 freq 3
	setcycle 16 key 54
	setcycle 16 loc 4
	setcycle 16 tp 0.6
	setcycle 17 block 3
	setcycle 17 freq 3
	setcycle 17 key 43
	setcycle 17 loc 3
	setcycle 17 tp 0.33
	setcycle 18 block 3
	setcycle 18 freq 1
	setcycle 18 key 37
	setcycle 18 loc 7
	setcycle 18 tp 0.2
	setcycle 19 block 3
	setcycle 19 freq 2
	setcycle 19 key 74
	setcycle 19 loc 4
	setcycle 19 tp 0.33
	setcycle 20 block 3
	setcycle 20 freq 2
	setcycle 20 key 47
	setcycle 20 loc 7
	setcycle 20 tp 0.22
	setcycle 21 block 3
	setcycle 21 freq 1
	setcycle 21 key 78
	setcycle 21 loc 8
	setcycle 21 tp 0.16
	setcycle 22 block 3
	setcycle 22 freq 2
	setcycle 22 key 82
	setcycle 22 loc 2
	setcycle 22 tp 0.66
	setcycle 23 block 3
	setcycle 23 freq 2
	setcycle 23 key 24
	setcycle 23 loc 4
	setcycle 23 tp 0.4
	setcycle 24 block 3
	setcycle 24 freq 1
	setcycle 24 key 45
	setcycle 24 loc 5
	setcycle 24 tp 0.11
	setcycle 25 block 3
	setcycle 25 freq 3
	setcycle 25 key 54
	setcycle 25 loc 4
	setcycle 25 tp 0.6
	setcycle 26 block 3
	setcycle 26 freq 2
	setcycle 26 key 47
	setcycle 26 loc 7
	setcycle 26 tp 0.22
	setcycle 27 block 3
	setcycle 27 freq 1
	setcycle 27 key 73
	setcycle 27 loc 3
	setcycle 27 tp 0.16
	setcycle 28 block 3
	setcycle 28 freq 1
	setcycle 28 key 34
	setcycle 28 loc 4
	setcycle 28 tp 0.2
	setcycle 29 block 3
	setcycle 29 freq 2
	setcycle 29 key 42
	setcycle 29 loc 2
	setcycle 29 tp 0.22
	setcycle 30 block 3
	setcycle 30 freq 1
	setcycle 30 key 23
	setcycle 30 loc 3
	setcycle 30 tp 0.2
	setcycle 31 block 3
	setcycle 31 freq 1
	setcycle 31 key 35
	setcycle 31 loc 5
	setcycle 31 tp 0.2
	setcycle 32 block 3
	setcycle 32 freq 1
	setcycle 32 key 57
	setcycle 32 loc 7
	setcycle 32 tp 0.2
	setcycle 33 block 3
	setcycle 33 freq 2
	setcycle 33 key 74
	setcycle 33 loc 4
	setcycle 33 tp 0.33
	setcycle 34 block 3
	setcycle 34 freq 1
	setcycle 34 key 44
	setcycle 34 loc 4
	setcycle 34 tp 0.11
	setcycle 35 block 3
	setcycle 35 freq 2
	setcycle 35 key 42
	setcycle 35 loc 2
	setcycle 35 tp 0.22
	setcycle 36 block 3
	setcycle 36 freq 1
	setcycle 36 key 27
	setcycle 36 loc 7
	setcycle 36 tp 0.2
	run trial_sequence_6

define loop block_4
	set source_file ""
	set source table
	set skip 0
	set repeat 1
	set order sequential
	set offset no
	set item trial_sequence
	set description "Repeatedly runs another item"
	set cycles 37
	set continuous no
	set column_order "loc_1;loc_2;loc_3;loc_4;correct_response;loc_5;loc_6;loc_8;loc_7"
	set break_if_on_first yes
	set break_if never
	setcycle 0 block 4
	setcycle 0 freq 2
	setcycle 0 key 71
	setcycle 0 loc 1
	setcycle 0 tp 0.33
	setcycle 1 block 4
	setcycle 1 freq 3
	setcycle 1 key 15
	setcycle 1 loc 5
	setcycle 1 tp 1
	setcycle 2 block 4
	setcycle 2 freq 3
	setcycle 2 key 54
	setcycle 2 loc 4
	setcycle 2 tp 0.6
	setcycle 3 block 4
	setcycle 3 freq 3
	setcycle 3 key 43
	setcycle 3 loc 3
	setcycle 3 tp 0.33
	setcycle 4 block 4
	setcycle 4 freq 1
	setcycle 4 key 36
	setcycle 4 loc 6
	setcycle 4 tp 0.2
	setcycle 5 block 4
	setcycle 5 freq 1
	setcycle 5 key 62
	setcycle 5 loc 2
	setcycle 5 tp 1
	setcycle 6 block 4
	setcycle 6 freq 1
	setcycle 6 key 28
	setcycle 6 loc 8
	setcycle 6 tp 0.2
	setcycle 7 block 4
	setcycle 7 freq 1
	setcycle 7 key 87
	setcycle 7 loc 7
	setcycle 7 tp 0.33
	setcycle 8 block 4
	setcycle 8 freq 2
	setcycle 8 key 71
	setcycle 8 loc 1
	setcycle 8 tp 0.33
	setcycle 9 block 4
	setcycle 9 freq 3
	setcycle 9 key 15
	setcycle 9 loc 5
	setcycle 9 tp 1
	setcycle 10 block 4
	setcycle 10 freq 1
	setcycle 10 key 58
	setcycle 10 loc 8
	setcycle 10 tp 0.2
	setcycle 11 block 4
	setcycle 11 freq 2
	setcycle 11 key 82
	setcycle 11 loc 2
	setcycle 11 tp 0.66
	setcycle 12 block 4
	setcycle 12 freq 2
	setcycle 12 key 24
	setcycle 12 loc 4
	setcycle 12 tp 0.4
	setcycle 13 block 4
	setcycle 13 freq 3
	setcycle 13 key 43
	setcycle 13 loc 3
	setcycle 13 tp 0.33
	setcycle 14 block 4
	setcycle 14 freq 1
	setcycle 14 key 31
	setcycle 14 loc 1
	setcycle 14 tp 0.2
	setcycle 15 block 4
	setcycle 15 freq 3
	setcycle 15 key 15
	setcycle 15 loc 5
	setcycle 15 tp 1
	setcycle 16 block 4
	setcycle 16 freq 3
	setcycle 16 key 54
	setcycle 16 loc 4
	setcycle 16 tp 0.6
	setcycle 17 block 4
	setcycle 17 freq 3
	setcycle 17 key 43
	setcycle 17 loc 3
	setcycle 17 tp 0.33
	setcycle 18 block 4
	setcycle 18 freq 1
	setcycle 18 key 37
	setcycle 18 loc 7
	setcycle 18 tp 0.2
	setcycle 19 block 4
	setcycle 19 freq 2
	setcycle 19 key 74
	setcycle 19 loc 4
	setcycle 19 tp 0.33
	setcycle 20 block 4
	setcycle 20 freq 2
	setcycle 20 key 47
	setcycle 20 loc 7
	setcycle 20 tp 0.22
	setcycle 21 block 4
	setcycle 21 freq 1
	setcycle 21 key 78
	setcycle 21 loc 8
	setcycle 21 tp 0.16
	setcycle 22 block 4
	setcycle 22 freq 2
	setcycle 22 key 82
	setcycle 22 loc 2
	setcycle 22 tp 0.66
	setcycle 23 block 4
	setcycle 23 freq 2
	setcycle 23 key 24
	setcycle 23 loc 4
	setcycle 23 tp 0.4
	setcycle 24 block 4
	setcycle 24 freq 1
	setcycle 24 key 45
	setcycle 24 loc 5
	setcycle 24 tp 0.11
	setcycle 25 block 4
	setcycle 25 freq 3
	setcycle 25 key 54
	setcycle 25 loc 4
	setcycle 25 tp 0.6
	setcycle 26 block 4
	setcycle 26 freq 2
	setcycle 26 key 47
	setcycle 26 loc 7
	setcycle 26 tp 0.22
	setcycle 27 block 4
	setcycle 27 freq 1
	setcycle 27 key 73
	setcycle 27 loc 3
	setcycle 27 tp 0.16
	setcycle 28 block 4
	setcycle 28 freq 1
	setcycle 28 key 34
	setcycle 28 loc 4
	setcycle 28 tp 0.2
	setcycle 29 block 4
	setcycle 29 freq 2
	setcycle 29 key 42
	setcycle 29 loc 2
	setcycle 29 tp 0.22
	setcycle 30 block 4
	setcycle 30 freq 1
	setcycle 30 key 23
	setcycle 30 loc 3
	setcycle 30 tp 0.2
	setcycle 31 block 4
	setcycle 31 freq 1
	setcycle 31 key 35
	setcycle 31 loc 5
	setcycle 31 tp 0.2
	setcycle 32 block 4
	setcycle 32 freq 1
	setcycle 32 key 57
	setcycle 32 loc 7
	setcycle 32 tp 0.2
	setcycle 33 block 4
	setcycle 33 freq 2
	setcycle 33 key 74
	setcycle 33 loc 4
	setcycle 33 tp 0.33
	setcycle 34 block 4
	setcycle 34 freq 1
	setcycle 34 key 44
	setcycle 34 loc 4
	setcycle 34 tp 0.11
	setcycle 35 block 4
	setcycle 35 freq 2
	setcycle 35 key 42
	setcycle 35 loc 2
	setcycle 35 tp 0.22
	setcycle 36 block 4
	setcycle 36 freq 1
	setcycle 36 key 27
	setcycle 36 loc 7
	setcycle 36 tp 0.2
	run trial_sequence_5

define loop block_5
	set source_file ""
	set source table
	set skip 0
	set repeat 1
	set order sequential
	set offset no
	set item trial_sequence
	set description "Repeatedly runs another item"
	set cycles 37
	set continuous no
	set column_order "loc_1;loc_2;loc_3;loc_4;correct_response;loc_5;loc_6;loc_8;loc_7"
	set break_if_on_first yes
	set break_if never
	setcycle 0 block 5
	setcycle 0 freq 2
	setcycle 0 key 71
	setcycle 0 loc 1
	setcycle 0 tp 0.33
	setcycle 1 block 5
	setcycle 1 freq 3
	setcycle 1 key 15
	setcycle 1 loc 5
	setcycle 1 tp 1
	setcycle 2 block 5
	setcycle 2 freq 3
	setcycle 2 key 54
	setcycle 2 loc 4
	setcycle 2 tp 0.6
	setcycle 3 block 5
	setcycle 3 freq 3
	setcycle 3 key 43
	setcycle 3 loc 3
	setcycle 3 tp 0.33
	setcycle 4 block 5
	setcycle 4 freq 1
	setcycle 4 key 36
	setcycle 4 loc 6
	setcycle 4 tp 0.2
	setcycle 5 block 5
	setcycle 5 freq 1
	setcycle 5 key 62
	setcycle 5 loc 2
	setcycle 5 tp 1
	setcycle 6 block 5
	setcycle 6 freq 1
	setcycle 6 key 28
	setcycle 6 loc 8
	setcycle 6 tp 0.2
	setcycle 7 block 5
	setcycle 7 freq 1
	setcycle 7 key 87
	setcycle 7 loc 7
	setcycle 7 tp 0.33
	setcycle 8 block 5
	setcycle 8 freq 2
	setcycle 8 key 71
	setcycle 8 loc 1
	setcycle 8 tp 0.33
	setcycle 9 block 5
	setcycle 9 freq 3
	setcycle 9 key 15
	setcycle 9 loc 5
	setcycle 9 tp 1
	setcycle 10 block 5
	setcycle 10 freq 1
	setcycle 10 key 58
	setcycle 10 loc 8
	setcycle 10 tp 0.2
	setcycle 11 block 5
	setcycle 11 freq 2
	setcycle 11 key 82
	setcycle 11 loc 2
	setcycle 11 tp 0.66
	setcycle 12 block 5
	setcycle 12 freq 2
	setcycle 12 key 24
	setcycle 12 loc 4
	setcycle 12 tp 0.4
	setcycle 13 block 5
	setcycle 13 freq 3
	setcycle 13 key 43
	setcycle 13 loc 3
	setcycle 13 tp 0.33
	setcycle 14 block 5
	setcycle 14 freq 1
	setcycle 14 key 31
	setcycle 14 loc 1
	setcycle 14 tp 0.2
	setcycle 15 block 5
	setcycle 15 freq 3
	setcycle 15 key 15
	setcycle 15 loc 5
	setcycle 15 tp 1
	setcycle 16 block 5
	setcycle 16 freq 3
	setcycle 16 key 54
	setcycle 16 loc 4
	setcycle 16 tp 0.6
	setcycle 17 block 5
	setcycle 17 freq 3
	setcycle 17 key 43
	setcycle 17 loc 3
	setcycle 17 tp 0.33
	setcycle 18 block 5
	setcycle 18 freq 1
	setcycle 18 key 37
	setcycle 18 loc 7
	setcycle 18 tp 0.2
	setcycle 19 block 5
	setcycle 19 freq 2
	setcycle 19 key 74
	setcycle 19 loc 4
	setcycle 19 tp 0.33
	setcycle 20 block 5
	setcycle 20 freq 2
	setcycle 20 key 47
	setcycle 20 loc 7
	setcycle 20 tp 0.22
	setcycle 21 block 5
	setcycle 21 freq 1
	setcycle 21 key 78
	setcycle 21 loc 8
	setcycle 21 tp 0.16
	setcycle 22 block 5
	setcycle 22 freq 2
	setcycle 22 key 82
	setcycle 22 loc 2
	setcycle 22 tp 0.66
	setcycle 23 block 5
	setcycle 23 freq 2
	setcycle 23 key 24
	setcycle 23 loc 4
	setcycle 23 tp 0.4
	setcycle 24 block 5
	setcycle 24 freq 1
	setcycle 24 key 45
	setcycle 24 loc 5
	setcycle 24 tp 0.11
	setcycle 25 block 5
	setcycle 25 freq 3
	setcycle 25 key 54
	setcycle 25 loc 4
	setcycle 25 tp 0.6
	setcycle 26 block 5
	setcycle 26 freq 2
	setcycle 26 key 47
	setcycle 26 loc 7
	setcycle 26 tp 0.22
	setcycle 27 block 5
	setcycle 27 freq 1
	setcycle 27 key 73
	setcycle 27 loc 3
	setcycle 27 tp 0.16
	setcycle 28 block 5
	setcycle 28 freq 1
	setcycle 28 key 34
	setcycle 28 loc 4
	setcycle 28 tp 0.2
	setcycle 29 block 5
	setcycle 29 freq 2
	setcycle 29 key 42
	setcycle 29 loc 2
	setcycle 29 tp 0.22
	setcycle 30 block 5
	setcycle 30 freq 1
	setcycle 30 key 23
	setcycle 30 loc 3
	setcycle 30 tp 0.2
	setcycle 31 block 5
	setcycle 31 freq 1
	setcycle 31 key 35
	setcycle 31 loc 5
	setcycle 31 tp 0.2
	setcycle 32 block 5
	setcycle 32 freq 1
	setcycle 32 key 57
	setcycle 32 loc 7
	setcycle 32 tp 0.2
	setcycle 33 block 5
	setcycle 33 freq 2
	setcycle 33 key 74
	setcycle 33 loc 4
	setcycle 33 tp 0.33
	setcycle 34 block 5
	setcycle 34 freq 1
	setcycle 34 key 44
	setcycle 34 loc 4
	setcycle 34 tp 0.11
	setcycle 35 block 5
	setcycle 35 freq 2
	setcycle 35 key 42
	setcycle 35 loc 2
	setcycle 35 tp 0.22
	setcycle 36 block 5
	setcycle 36 freq 1
	setcycle 36 key 27
	setcycle 36 loc 7
	setcycle 36 tp 0.2
	run trial_sequence_7

define sequence experiment
	set flush_keyboard yes
	set description "The main sequence of the experiment"
	run Sex always
	run Age always
	run Consent always
	run Instructions always
	run new_sketchpad always
	run Prac_block always
	run new_reset_feedback always
	run new_sketchpad_1 always
	run block_1 always
	run block_2 always
	run block_3 always
	run block_4 always
	run block_5 always
	run incongruent_block always
	run feedback always
	run notes never

define feedback feedback
	set reset_variables yes
	set duration mouseclick
	set description "Provides feedback to the participant"
	draw textline center=1 color="#000000" font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=always text="Thank you for taking part<br />Your average response time was [avg_rt]ms,<br />you scored [total_correct]/222;<br />your accuracy was [acc]%" x=0 y=0 z_index=0

define loop incongruent_block
	set source_file ""
	set source table
	set skip 0
	set repeat 1
	set order sequential
	set offset no
	set item trial_sequence_2
	set description "Repeatedly runs another item"
	set cycles 37
	set continuous no
	set column_order "loc_1;loc_2;loc_3;loc_4;correct_response;loc_5;loc_6;loc_7;loc_8"
	set break_if_on_first yes
	set break_if never
	setcycle 0 block 6
	setcycle 0 key 71
	setcycle 0 loc 1
	setcycle 1 block 6
	setcycle 1 key 12
	setcycle 1 loc 2
	setcycle 2 block 6
	setcycle 2 key 24
	setcycle 2 loc 4
	setcycle 3 block 6
	setcycle 3 key 43
	setcycle 3 loc 3
	setcycle 4 block 6
	setcycle 4 key 32
	setcycle 4 loc 2
	setcycle 5 block 6
	setcycle 5 key 21
	setcycle 5 loc 1
	setcycle 6 block 6
	setcycle 6 key 15
	setcycle 6 loc 5
	setcycle 7 block 6
	setcycle 7 key 51
	setcycle 7 loc 1
	setcycle 8 block 6
	setcycle 8 key 17
	setcycle 8 loc 7
	setcycle 9 block 6
	setcycle 9 key 71
	setcycle 9 loc 1
	setcycle 10 block 6
	setcycle 10 key 11
	setcycle 10 loc 1
	setcycle 11 block 6
	setcycle 11 key 18
	setcycle 11 loc 8
	setcycle 12 block 6
	setcycle 12 key 84
	setcycle 12 loc 4
	setcycle 13 block 6
	setcycle 13 key 44
	setcycle 13 loc 4
	setcycle 14 block 6
	setcycle 14 key 45
	setcycle 14 loc 5
	setcycle 15 block 6
	setcycle 15 key 53
	setcycle 15 loc 3
	setcycle 16 block 6
	setcycle 16 key 33
	setcycle 16 loc 3
	setcycle 17 block 6
	setcycle 17 key 35
	setcycle 17 loc 5
	setcycle 18 block 6
	setcycle 18 key 54
	setcycle 18 loc 4
	setcycle 19 block 6
	setcycle 19 key 46
	setcycle 19 loc 6
	setcycle 20 block 6
	setcycle 20 key 62
	setcycle 20 loc 2
	setcycle 21 block 6
	setcycle 21 key 22
	setcycle 21 loc 2
	setcycle 22 block 6
	setcycle 22 key 25
	setcycle 22 loc 5
	setcycle 23 block 6
	setcycle 23 key 55
	setcycle 23 loc 5
	setcycle 24 block 6
	setcycle 24 key 56
	setcycle 24 loc 6
	setcycle 25 block 6
	setcycle 25 key 62
	setcycle 25 loc 2
	setcycle 26 block 6
	setcycle 26 key 26
	setcycle 26 loc 6
	setcycle 27 block 6
	setcycle 27 key 65
	setcycle 27 loc 5
	setcycle 28 block 6
	setcycle 28 key 57
	setcycle 28 loc 7
	setcycle 29 block 6
	setcycle 29 key 73
	setcycle 29 loc 3
	setcycle 30 block 6
	setcycle 30 key 36
	setcycle 30 loc 6
	setcycle 31 block 6
	setcycle 31 key 67
	setcycle 31 loc 7
	setcycle 32 block 6
	setcycle 32 key 74
	setcycle 32 loc 4
	setcycle 33 block 6
	setcycle 33 key 47
	setcycle 33 loc 7
	setcycle 34 block 6
	setcycle 34 key 75
	setcycle 34 loc 5
	setcycle 35 block 6
	setcycle 35 key 58
	setcycle 35 loc 8
	setcycle 36 block 6
	setcycle 36 key 84
	setcycle 36 loc 4
	run trial_sequence_2

define feedback new_feedback_1
	set reset_variables yes
	set duration 0
	set description "Provides feedback to the participant"

define logger new_logger_5
	set description "Logs experimental data"
	set auto_log yes

define logger new_logger_5_1
	set description "Logs experimental data"
	set auto_log yes

define logger new_logger_5_2
	set description "Logs experimental data"
	set auto_log yes

define logger new_logger_5_3
	set description "Logs experimental data"
	set auto_log yes

define logger new_logger_5_4
	set description "Logs experimental data"
	set auto_log yes

define logger new_logger_5_5
	set description "Logs experimental data"
	set auto_log yes

define reset_feedback new_reset_feedback
	set description "Resets the feedback variables, such as 'avg_rt' and 'acc'"

define sketchpad new_sketchpad
	set duration mouseclick
	set description "Displays stimuli"
	draw textline center=1 color="#000000" font_bold=no font_family=mono font_italic=no font_size=40 html=yes show_if=always text="Tap to begin the practice block" x=0 y=0 z_index=0

define sketchpad new_sketchpad_1
	set duration mouseclick
	set description "Displays stimuli"
	draw textline center=1 color="#000000" font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=always text="The practice has now finished<br /><br />Please speak to the experimenter if you have any questions, <br />otherwise tap the screen to begin the main experiment" x=0 y=0 z_index=0

define sketchpad new_sketchpad_11
	# orthogonal separation = 98 pixels, diagonal separation = 138.59 pixels
	set duration 0
	set description "Displays stimuli"
	draw rect color="#ffff00" fill=1 h=200 penwidth=1 show_if=always w=200 x=-552 y=-240 z_index=8
	draw rect color="#00ffff" fill=1 h=200 penwidth=1 show_if=always w=200 x=-254 y=-240 z_index=7
	draw rect color="#00ff00" fill=1 h=200 penwidth=1 show_if=always w=200 x=44 y=-240 z_index=6
	draw rect color="#ff5500" fill=1 h=200 penwidth=1 show_if=always w=200 x=342 y=-240 z_index=5
	draw rect color="#ff0000" fill=1 h=200 penwidth=1 show_if=always w=200 x=-552 y=48 z_index=4
	draw rect color="#aaaaff" fill=1 h=200 penwidth=1 show_if=always w=200 x=-254 y=48 z_index=3
	draw rect color="#0000ff" fill=1 h=200 penwidth=1 show_if=always w=200 x=44 y=48 z_index=2
	draw rect color="#ff00ff" fill=1 h=200 penwidth=1 show_if=always w=200 x=342 y=48 z_index=1
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=1" x=-448 y=-140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=2" x=-150 y=-140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=3" x=148 y=-140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=4" x=446 y=-140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=5" x=-448 y=140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=6" x=-150 y=140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=7" x=148 y=140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=8" x=448 y=140 z_index=0

define sketchpad new_sketchpad_11_1
	# orthogonal separation = 98 pixels, diagonal separation = 138.59 pixels
	set duration 0
	set description "Displays stimuli"
	draw rect color="#ffff00" fill=1 h=200 penwidth=1 show_if=always w=200 x=-552 y=-240 z_index=8
	draw rect color="#00ffff" fill=1 h=200 penwidth=1 show_if=always w=200 x=-254 y=-240 z_index=7
	draw rect color="#00ff00" fill=1 h=200 penwidth=1 show_if=always w=200 x=44 y=-240 z_index=6
	draw rect color="#ff5500" fill=1 h=200 penwidth=1 show_if=always w=200 x=342 y=-240 z_index=5
	draw rect color="#ff0000" fill=1 h=200 penwidth=1 show_if=always w=200 x=-552 y=48 z_index=4
	draw rect color="#aaaaff" fill=1 h=200 penwidth=1 show_if=always w=200 x=-254 y=48 z_index=3
	draw rect color="#0000ff" fill=1 h=200 penwidth=1 show_if=always w=200 x=44 y=48 z_index=2
	draw rect color="#ff00ff" fill=1 h=200 penwidth=1 show_if=always w=200 x=342 y=48 z_index=1

define sketchpad new_sketchpad_11_1_1
	# orthogonal separation = 98 pixels, diagonal separation = 138.59 pixels
	set duration 0
	set description "Displays stimuli"
	draw rect color="#ffff00" fill=1 h=200 penwidth=1 show_if=always w=200 x=-552 y=-240 z_index=8
	draw rect color="#00ffff" fill=1 h=200 penwidth=1 show_if=always w=200 x=-254 y=-240 z_index=7
	draw rect color="#00ff00" fill=1 h=200 penwidth=1 show_if=always w=200 x=44 y=-240 z_index=6
	draw rect color="#ff5500" fill=1 h=200 penwidth=1 show_if=always w=200 x=342 y=-240 z_index=5
	draw rect color="#ff0000" fill=1 h=200 penwidth=1 show_if=always w=200 x=-552 y=48 z_index=4
	draw rect color="#aaaaff" fill=1 h=200 penwidth=1 show_if=always w=200 x=-254 y=48 z_index=3
	draw rect color="#0000ff" fill=1 h=200 penwidth=1 show_if=always w=200 x=44 y=48 z_index=2
	draw rect color="#ff00ff" fill=1 h=200 penwidth=1 show_if=always w=200 x=342 y=48 z_index=1

define sketchpad new_sketchpad_11_1_2
	# orthogonal separation = 98 pixels, diagonal separation = 138.59 pixels
	set duration 0
	set description "Displays stimuli"
	draw rect color="#ffff00" fill=1 h=200 penwidth=1 show_if=always w=200 x=-552 y=-240 z_index=8
	draw rect color="#00ffff" fill=1 h=200 penwidth=1 show_if=always w=200 x=-254 y=-240 z_index=7
	draw rect color="#00ff00" fill=1 h=200 penwidth=1 show_if=always w=200 x=44 y=-240 z_index=6
	draw rect color="#ff5500" fill=1 h=200 penwidth=1 show_if=always w=200 x=342 y=-240 z_index=5
	draw rect color="#ff0000" fill=1 h=200 penwidth=1 show_if=always w=200 x=-552 y=48 z_index=4
	draw rect color="#aaaaff" fill=1 h=200 penwidth=1 show_if=always w=200 x=-254 y=48 z_index=3
	draw rect color="#0000ff" fill=1 h=200 penwidth=1 show_if=always w=200 x=44 y=48 z_index=2
	draw rect color="#ff00ff" fill=1 h=200 penwidth=1 show_if=always w=200 x=342 y=48 z_index=1

define sketchpad new_sketchpad_11_1_3
	# orthogonal separation = 98 pixels, diagonal separation = 138.59 pixels
	set duration 0
	set description "Displays stimuli"
	draw rect color="#ffff00" fill=1 h=200 penwidth=1 show_if=always w=200 x=-552 y=-240 z_index=8
	draw rect color="#00ffff" fill=1 h=200 penwidth=1 show_if=always w=200 x=-254 y=-240 z_index=7
	draw rect color="#00ff00" fill=1 h=200 penwidth=1 show_if=always w=200 x=44 y=-240 z_index=6
	draw rect color="#ff5500" fill=1 h=200 penwidth=1 show_if=always w=200 x=342 y=-240 z_index=5
	draw rect color="#ff0000" fill=1 h=200 penwidth=1 show_if=always w=200 x=-552 y=48 z_index=4
	draw rect color="#aaaaff" fill=1 h=200 penwidth=1 show_if=always w=200 x=-254 y=48 z_index=3
	draw rect color="#0000ff" fill=1 h=200 penwidth=1 show_if=always w=200 x=44 y=48 z_index=2
	draw rect color="#ff00ff" fill=1 h=200 penwidth=1 show_if=always w=200 x=342 y=48 z_index=1

define sketchpad new_sketchpad_11_1_4
	# orthogonal separation = 98 pixels, diagonal separation = 138.59 pixels
	set duration 0
	set description "Displays stimuli"
	draw rect color="#ffff00" fill=1 h=200 penwidth=1 show_if=always w=200 x=-552 y=-240 z_index=8
	draw rect color="#00ffff" fill=1 h=200 penwidth=1 show_if=always w=200 x=-254 y=-240 z_index=7
	draw rect color="#00ff00" fill=1 h=200 penwidth=1 show_if=always w=200 x=44 y=-240 z_index=6
	draw rect color="#ff5500" fill=1 h=200 penwidth=1 show_if=always w=200 x=342 y=-240 z_index=5
	draw rect color="#ff0000" fill=1 h=200 penwidth=1 show_if=always w=200 x=-552 y=48 z_index=4
	draw rect color="#aaaaff" fill=1 h=200 penwidth=1 show_if=always w=200 x=-254 y=48 z_index=3
	draw rect color="#0000ff" fill=1 h=200 penwidth=1 show_if=always w=200 x=44 y=48 z_index=2
	draw rect color="#ff00ff" fill=1 h=200 penwidth=1 show_if=always w=200 x=342 y=48 z_index=1

define sketchpad new_sketchpad_11_1_5
	# orthogonal separation = 98 pixels, diagonal separation = 138.59 pixels
	set duration 0
	set description "Displays stimuli"
	draw rect color="#ffff00" fill=1 h=200 penwidth=1 show_if=always w=200 x=-552 y=-240 z_index=8
	draw rect color="#00ffff" fill=1 h=200 penwidth=1 show_if=always w=200 x=-254 y=-240 z_index=7
	draw rect color="#00ff00" fill=1 h=200 penwidth=1 show_if=always w=200 x=44 y=-240 z_index=6
	draw rect color="#ff5500" fill=1 h=200 penwidth=1 show_if=always w=200 x=342 y=-240 z_index=5
	draw rect color="#ff0000" fill=1 h=200 penwidth=1 show_if=always w=200 x=-552 y=48 z_index=4
	draw rect color="#aaaaff" fill=1 h=200 penwidth=1 show_if=always w=200 x=-254 y=48 z_index=3
	draw rect color="#0000ff" fill=1 h=200 penwidth=1 show_if=always w=200 x=44 y=48 z_index=2
	draw rect color="#ff00ff" fill=1 h=200 penwidth=1 show_if=always w=200 x=342 y=48 z_index=1

define sketchpad new_sketchpad_11_2
	# orthogonal separation = 98 pixels, diagonal separation = 138.59 pixels
	set duration 0
	set description "Displays stimuli"
	draw rect color="#ffff00" fill=1 h=200 penwidth=1 show_if=always w=200 x=-552 y=-240 z_index=8
	draw rect color="#00ffff" fill=1 h=200 penwidth=1 show_if=always w=200 x=-254 y=-240 z_index=7
	draw rect color="#00ff00" fill=1 h=200 penwidth=1 show_if=always w=200 x=44 y=-240 z_index=6
	draw rect color="#ff5500" fill=1 h=200 penwidth=1 show_if=always w=200 x=342 y=-240 z_index=5
	draw rect color="#ff0000" fill=1 h=200 penwidth=1 show_if=always w=200 x=-552 y=48 z_index=4
	draw rect color="#aaaaff" fill=1 h=200 penwidth=1 show_if=always w=200 x=-254 y=48 z_index=3
	draw rect color="#0000ff" fill=1 h=200 penwidth=1 show_if=always w=200 x=44 y=48 z_index=2
	draw rect color="#ff00ff" fill=1 h=200 penwidth=1 show_if=always w=200 x=342 y=48 z_index=1
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=1" x=-448 y=-140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=2" x=-150 y=-140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=3" x=148 y=-140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=4" x=446 y=-140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=5" x=-448 y=140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=6" x=-150 y=140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=7" x=148 y=140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=8" x=448 y=140 z_index=0

define sketchpad new_sketchpad_11_3
	# orthogonal separation = 98 pixels, diagonal separation = 138.59 pixels
	set duration 0
	set description "Displays stimuli"
	draw rect color="#ffff00" fill=1 h=200 penwidth=1 show_if=always w=200 x=-552 y=-240 z_index=8
	draw rect color="#00ffff" fill=1 h=200 penwidth=1 show_if=always w=200 x=-254 y=-240 z_index=7
	draw rect color="#00ff00" fill=1 h=200 penwidth=1 show_if=always w=200 x=44 y=-240 z_index=6
	draw rect color="#ff5500" fill=1 h=200 penwidth=1 show_if=always w=200 x=342 y=-240 z_index=5
	draw rect color="#ff0000" fill=1 h=200 penwidth=1 show_if=always w=200 x=-552 y=48 z_index=4
	draw rect color="#aaaaff" fill=1 h=200 penwidth=1 show_if=always w=200 x=-254 y=48 z_index=3
	draw rect color="#0000ff" fill=1 h=200 penwidth=1 show_if=always w=200 x=44 y=48 z_index=2
	draw rect color="#ff00ff" fill=1 h=200 penwidth=1 show_if=always w=200 x=342 y=48 z_index=1
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=1" x=-448 y=-140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=2" x=-150 y=-140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=3" x=148 y=-140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=4" x=446 y=-140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=5" x=-448 y=140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=6" x=-150 y=140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=7" x=148 y=140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=8" x=448 y=140 z_index=0

define sketchpad new_sketchpad_11_4
	# orthogonal separation = 98 pixels, diagonal separation = 138.59 pixels
	set duration 0
	set description "Displays stimuli"
	draw rect color="#ffff00" fill=1 h=200 penwidth=1 show_if=always w=200 x=-552 y=-240 z_index=8
	draw rect color="#00ffff" fill=1 h=200 penwidth=1 show_if=always w=200 x=-254 y=-240 z_index=7
	draw rect color="#00ff00" fill=1 h=200 penwidth=1 show_if=always w=200 x=44 y=-240 z_index=6
	draw rect color="#ff5500" fill=1 h=200 penwidth=1 show_if=always w=200 x=342 y=-240 z_index=5
	draw rect color="#ff0000" fill=1 h=200 penwidth=1 show_if=always w=200 x=-552 y=48 z_index=4
	draw rect color="#aaaaff" fill=1 h=200 penwidth=1 show_if=always w=200 x=-254 y=48 z_index=3
	draw rect color="#0000ff" fill=1 h=200 penwidth=1 show_if=always w=200 x=44 y=48 z_index=2
	draw rect color="#ff00ff" fill=1 h=200 penwidth=1 show_if=always w=200 x=342 y=48 z_index=1
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=1" x=-448 y=-140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=2" x=-150 y=-140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=3" x=148 y=-140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=4" x=446 y=-140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=5" x=-448 y=140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=6" x=-150 y=140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=7" x=148 y=140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=8" x=448 y=140 z_index=0

define sketchpad new_sketchpad_11_5
	# orthogonal separation = 98 pixels, diagonal separation = 138.59 pixels
	set duration 0
	set description "Displays stimuli"
	draw rect color="#ffff00" fill=1 h=200 penwidth=1 show_if=always w=200 x=-552 y=-240 z_index=8
	draw rect color="#00ffff" fill=1 h=200 penwidth=1 show_if=always w=200 x=-254 y=-240 z_index=7
	draw rect color="#00ff00" fill=1 h=200 penwidth=1 show_if=always w=200 x=44 y=-240 z_index=6
	draw rect color="#ff5500" fill=1 h=200 penwidth=1 show_if=always w=200 x=342 y=-240 z_index=5
	draw rect color="#ff0000" fill=1 h=200 penwidth=1 show_if=always w=200 x=-552 y=48 z_index=4
	draw rect color="#aaaaff" fill=1 h=200 penwidth=1 show_if=always w=200 x=-254 y=48 z_index=3
	draw rect color="#0000ff" fill=1 h=200 penwidth=1 show_if=always w=200 x=44 y=48 z_index=2
	draw rect color="#ff00ff" fill=1 h=200 penwidth=1 show_if=always w=200 x=342 y=48 z_index=1
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=1" x=-448 y=-140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=2" x=-150 y=-140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=3" x=148 y=-140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=4" x=446 y=-140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=5" x=-448 y=140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=6" x=-150 y=140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=7" x=148 y=140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=8" x=448 y=140 z_index=0

define sketchpad new_sketchpad_11_6
	# orthogonal separation = 98 pixels, diagonal separation = 138.59 pixels
	set duration 0
	set description "Displays stimuli"
	draw rect color="#ffff00" fill=1 h=200 penwidth=1 show_if=always w=200 x=-552 y=-240 z_index=8
	draw rect color="#00ffff" fill=1 h=200 penwidth=1 show_if=always w=200 x=-254 y=-240 z_index=7
	draw rect color="#00ff00" fill=1 h=200 penwidth=1 show_if=always w=200 x=44 y=-240 z_index=6
	draw rect color="#ff5500" fill=1 h=200 penwidth=1 show_if=always w=200 x=342 y=-240 z_index=5
	draw rect color="#ff0000" fill=1 h=200 penwidth=1 show_if=always w=200 x=-552 y=48 z_index=4
	draw rect color="#aaaaff" fill=1 h=200 penwidth=1 show_if=always w=200 x=-254 y=48 z_index=3
	draw rect color="#0000ff" fill=1 h=200 penwidth=1 show_if=always w=200 x=44 y=48 z_index=2
	draw rect color="#ff00ff" fill=1 h=200 penwidth=1 show_if=always w=200 x=342 y=48 z_index=1
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=1" x=-448 y=-140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=2" x=-150 y=-140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=3" x=148 y=-140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=4" x=446 y=-140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=5" x=-448 y=140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=6" x=-150 y=140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=7" x=148 y=140 z_index=0
	draw image center=1 file="star.png" scale=0.15 show_if="[loc]=8" x=448 y=140 z_index=0

define touch_response new_touch_response_4
	set timeout 10000
	set show_cursor yes
	set flush yes
	set duration mouseclick
	set description "A grid-based response item, convenient for touch screens"
	set correct_response "[loc]"
	set _nrow 2
	set _ncol 4

define touch_response new_touch_response_4_1
	set timeout 10000
	set show_cursor yes
	set flush yes
	set duration mouseclick
	set description "A grid-based response item, convenient for touch screens"
	set correct_response "[loc]"
	set _nrow 2
	set _ncol 4

define touch_response new_touch_response_4_2
	set timeout 10000
	set show_cursor yes
	set flush yes
	set duration mouseclick
	set description "A grid-based response item, convenient for touch screens"
	set correct_response "[loc]"
	set _nrow 2
	set _ncol 4

define touch_response new_touch_response_4_3
	set timeout 10000
	set show_cursor yes
	set flush yes
	set duration mouseclick
	set description "A grid-based response item, convenient for touch screens"
	set correct_response "[loc]"
	set _nrow 2
	set _ncol 4

define touch_response new_touch_response_4_4
	set timeout 10000
	set show_cursor yes
	set flush yes
	set duration mouseclick
	set description "A grid-based response item, convenient for touch screens"
	set correct_response "[loc]"
	set _nrow 2
	set _ncol 4

define touch_response new_touch_response_4_5
	set timeout 10000
	set show_cursor yes
	set flush yes
	set duration mouseclick
	set description "A grid-based response item, convenient for touch screens"
	set correct_response "[loc]"
	set _nrow 2
	set _ncol 4

define sketchpad notes
	set duration 0
	set description "Displays stimuli"
	draw textline center=1 color="#000000" font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=always text="Key comparisons<br /><br />15 (freq 3, TP 1) - 43 (freq 3, TP .33)<br />62 (freq 1, TP 1) - 87 (freq 1, TP .33)<br />15 (freq 3, TP 1) - 62 (freq 1, TP 1)<br />43 (freq 3, TP .33) - 87 (freq 1, TP .33)" x=0 y=-32 z_index=0

define sequence trial_sequence_1
	set flush_keyboard yes
	set description "Runs a number of items in sequence"
	run new_sketchpad_11_2 always
	run new_touch_response_4_1 always
	run new_sketchpad_11_1_1 always
	run new_logger_5_1 always

define sequence trial_sequence_2
	set flush_keyboard yes
	set description "Runs a number of items in sequence"
	run new_sketchpad_11 always
	run new_touch_response_4 always
	run new_sketchpad_11_1 always
	run new_logger_5 always

define sequence trial_sequence_3
	set flush_keyboard yes
	set description "Runs a number of items in sequence"
	run new_sketchpad_11 always
	run new_touch_response_4 always
	run new_sketchpad_11_1 always
	run new_logger_5 always

define sequence trial_sequence_4
	set flush_keyboard yes
	set description "Runs a number of items in sequence"
	run new_sketchpad_11_3 always
	run new_touch_response_4_2 always
	run new_sketchpad_11_1_2 always
	run new_logger_5_2 always

define sequence trial_sequence_5
	set flush_keyboard yes
	set description "Runs a number of items in sequence"
	run new_sketchpad_11_4 always
	run new_touch_response_4_3 always
	run new_sketchpad_11_1_3 always
	run new_logger_5_3 always

define sequence trial_sequence_6
	set flush_keyboard yes
	set description "Runs a number of items in sequence"
	run new_sketchpad_11_5 always
	run new_touch_response_4_4 always
	run new_sketchpad_11_1_4 always
	run new_logger_5_4 always

define sequence trial_sequence_7
	set flush_keyboard yes
	set description "Runs a number of items in sequence"
	run new_sketchpad_11_6 always
	run new_touch_response_4_5 always
	run new_sketchpad_11_1_5 always
	run new_logger_5_5 always

