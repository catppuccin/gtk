#! /usr/bin/env bash

for theme in '' '-Purple' '-Pink' '-Red' '-Orange' '-Yellow' '-Green' '-Teal' '-Grey'; do
  for type in '' '-Nord' '-Dracula' '-Catppuccin-mocha' '-Catppuccin-macchiato' '-Catppuccin-frappe' '-Catppuccin-latte'; do
    case "$theme" in
      '')
        theme_color_dark='#3c84f7'
        theme_color_light='#5b9bf8'
        ;;
      -Purple)
        theme_color_dark='#AB47BC'
        theme_color_light='#BA68C8'
        ;;
      -Pink)
        theme_color_dark='#EC407A'
        theme_color_light='#F06292'
        ;;
      -Red)
        theme_color_dark='#E53935'
        theme_color_light='#F44336'
        ;;
      -Orange)
        theme_color_dark='#F57C00'
        theme_color_light='#FB8C00'
        ;;
      -Yellow)
        theme_color_dark='#FBC02D'
        theme_color_light='#FFD600'
        ;;
      -Green)
        theme_color_dark='#4CAF50'
        theme_color_light='#66BB6A'
        ;;
      -Teal)
        theme_color_dark='#009688'
        theme_color_light='#4DB6AC'
        ;;
      -Grey)
        theme_color_dark='#464646'
        theme_color_light='#DDDDDD'
        ;;
    esac

    if [[ "$type" == '-Nord' ]]; then
      case "$theme" in
        '')
          theme_color_dark='#5e81ac'
          theme_color_light='#89a3c2'
          ;;
        -Purple)
          theme_color_dark='#b57daa'
          theme_color_light='#c89dbf'
          ;;
        -Pink)
          theme_color_dark='#cd7092'
          theme_color_light='#dc98b1'
          ;;
        -Red)
          theme_color_dark='#c35b65'
          theme_color_light='#d4878f'
          ;;
        -Orange)
          theme_color_dark='#d0846c'
          theme_color_light='#dca493'
          ;;
        -Yellow)
          theme_color_dark='#e4b558'
          theme_color_light='#eac985'
          ;;
        -Green)
          theme_color_dark='#82ac5d'
          theme_color_light='#a0c082'
          ;;
        -Teal)
          theme_color_dark='#63a6a5'
          theme_color_light='#83b9b8'
          ;;
        -Grey)
          theme_color_dark='#3a4150'
          theme_color_light='#d9dce3'
          ;;
      esac
    fi

    if [[ "$type" == '-Dracula' ]]; then
      case "$theme" in
        '')
          theme_color_dark='#a679ec'
          theme_color_light='#bd93f9'
          ;;
        -Purple)
          theme_color_dark='#a679ec'
          theme_color_light='#bd93f9'
          ;;
        -Pink)
          theme_color_dark='#f04cab'
          theme_color_light='#ff79c6'
          ;;
        -Red)
          theme_color_dark='#f44d4d'
          theme_color_light='#ff5555'
          ;;
        -Orange)
          theme_color_dark='#f8a854'
          theme_color_light='#ffb86c'
          ;;
        -Yellow)
          theme_color_dark='#e8f467'
          theme_color_light='#f1fa8c'
          ;;
        -Green)
          theme_color_dark='#4be772'
          theme_color_light='#50fa7b'
          ;;
        -Teal)
          theme_color_dark='#20eed9'
          theme_color_light='#50fae9'
          ;;
        -Grey)
          theme_color_dark='#3c3f51'
          theme_color_light='#d9dae3'
          ;;
      esac
    fi

   if [[ "$type" == '-Catppuccin-mocha' ]]; then
      case "$theme" in
        '')
          theme_color_dark='#cba6f7'
          theme_color_light='#8839ef'
          ;;
        -Purple)
          theme_color_dark='#cba6f7'
          theme_color_light='#8839ef'
          ;;
        -Pink)
          theme_color_dark='#f5c2e7'
          theme_color_light='#ea76cb'
          ;;
        -Red)
          theme_color_dark='#f38ba8'
          theme_color_light='#d20f39'
          ;;
        -Orange)
          theme_color_dark='#fab387'
          theme_color_light='#fe640b'
          ;;
        -Yellow)
          theme_color_dark='#f9e2af'
          theme_color_light='#df8e1d'
          ;;
        -Green)
          theme_color_dark='#a6e3a1'
          theme_color_light='#40a02b'
          ;;
        -Teal)
          theme_color_dark='#94e2d5'
          theme_color_light='#179299'
          ;;
        -Grey)
          theme_color_dark='#a6adc8'
          theme_color_light='#6c6f85'
          ;;
      esac
    fi

    if [[ "$type" == '-Catppuccin-macchiato' ]]; then
      case "$theme" in
        '')
          theme_color_dark='#c6a0f6'
          theme_color_light='#d7bcf9'
          ;;
        -Purple)
          theme_color_dark='#c6a0f6'
          theme_color_light='#d7bcf9'
          ;;
        -Pink)
          theme_color_dark='#f5bde6'
          theme_color_light='#f8d1ed'
          ;;
        -Red)
          theme_color_dark='#ed8796'
          theme_color_light='#f2abb5'
          ;;
        -Orange)
          theme_color_dark='#f5a97f'
          theme_color_light='#f8c3a5'
          ;;
        -Yellow)
          theme_color_dark='#eed49f'
          theme_color_light='#f3e1bc'
          ;;
        -Green)
          theme_color_dark='#a6da95'
          theme_color_light='#c1e5b5'
          ;;
        -Teal)
          theme_color_dark='#8bd5ca'
          theme_color_light='#afe2da'
          ;;
        -Grey)
          theme_color_dark='#a5adcb'
          theme_color_light='#c0c6d0'
          ;;
      esac
    fi

    if [[ "$type" == '-Catppuccin-frappe' ]]; then
      case "$theme" in
        '')
          theme_color_dark='#ca9ee6'
          theme_color_light='#ead8f5'
          ;;
        -Purple)
          theme_color_dark='#ca9ee6'
          theme_color_light='#ead8f5'
          ;;
        -Pink)
          theme_color_dark='#f4b8e4'
          theme_color_light='#fbe3f4'
          ;;
        -Red)
          theme_color_dark='#e78284'
          theme_color_light='#f5cdce'
          ;;
        -Orange)
          theme_color_dark='#ef9f76'
          theme_color_light='#f9d9c8'
          ;;
        -Yellow)
          theme_color_dark='#e5c890'
          theme_color_light='#f5e9d3'
          ;;
        -Green)
          theme_color_dark='#a6d189'
          theme_color_light='#dbedd0'
          ;;
        -Teal)
          theme_color_dark='#81c8be'
          theme_color_light='#cde9e5'
          ;;
        -Grey)
          theme_color_dark='#a5adce'
          theme_color_light='#c0c6dd'
          ;;
      esac
    fi
    if [[ "$type" == '-Catppuccin-latte' ]]; then
      case "$theme" in
        '')
          theme_color_dark='#8839ef'
          theme_color_light='#cfb0f9'
          ;;
        -Purple)
          theme_color_dark='#8839ef'
          theme_color_light='#cfb0f9'
          ;;
        -Pink)
          theme_color_dark='#ea77cb'
          theme_color_light='#f7c8ea'
          ;;
        -Red)
          theme_color_dark='#d20f39'
          theme_color_light='#f795aa'
          ;;
        -Orange)
          theme_color_dark='#fe640b'
          theme_color_light='#ffc19d'
          ;;
        -Yellow)
          theme_color_dark='#df8e1d'
          theme_color_light='#f3d2a4'
          ;;
        -Green)
          theme_color_dark='#40a02b'
          theme_color_light='#abe59e'
          ;;
        -Teal)
          theme_color_dark='#179299'
          theme_color_light='#8be8ee'
          ;;
        -Grey)
          theme_color_dark='#a5adce'
          theme_color_light='#dbdeeb'
          ;;
      esac
    fi
    if [[ "$type" != '' ]]; then
      rm -rf "theme${theme}${type}"
      cp -rf "theme" "theme${theme}${type}"
      sed -i "s/#3c84f7/${theme_color_dark}/g" "theme${theme}${type}"/*.svg
      sed -i "s/#5b9bf8/${theme_color_light}/g" "theme${theme}${type}"/*.svg
    elif [[ "$theme" != '' ]]; then
      rm -rf "theme${theme}"
      cp -rf "theme" "theme${theme}"
      sed -i "s/#3c84f7/${theme_color_dark}/g" "theme${theme}"/*.svg
      sed -i "s/#5b9bf8/${theme_color_light}/g" "theme${theme}"/*.svg
    fi
  done
done

echo -e "DONE!"
