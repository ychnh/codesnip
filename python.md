copy_def_tiles_cmd = 'ln -s '+defualt_tile_dir+'/* '+compile_dir
subprocess.Popen( copy_def_tiles_cmd , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
