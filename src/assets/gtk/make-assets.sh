#! /usr/bin/env bash

for theme in '' '-Purple' '-Pink' '-Red' '-Orange' '-Yellow' '-Green' '-Teal' '-Grey'; do
  for type in '' '-Nord' '-Dracula'; do
    case "$theme" in
      '')
        theme_color_dark='#8caaee'
        theme_color_light='#8caaee'
        ;;
      -Purple)
        theme_color_dark='#ca9ee6'
        theme_color_light='#ca9ee6'
        ;;
      -Pink)
        theme_color_dark='#f4b8e4'
        theme_color_light='#f4b8e4'
        ;;
      -Red)
        theme_color_dark='#e78284'
        theme_color_light='#e78284'
        ;;
      -Orange)
        theme_color_dark='#ef9f76'
        theme_color_light='#ef9f76'
        ;;
      -Yellow)
        theme_color_dark='#e5c890'
        theme_color_light='#e5c890'
        ;;
      -Green)
        theme_color_dark='#a6d189'
        theme_color_light='#a6d189'
        ;;
      -Teal)
        theme_color_dark='#babbf1'
        theme_color_light='#babbf1'
        ;;
      -Grey)
        theme_color_dark='#ccd0da'
        theme_color_light='#ccd0da'
        ;;
    esac

    if [[ "$type" == '-Nord' ]]; then
      background_light='#f0f1f4'
      background_dark='#242932'
      base_dark='#1c1f26'
      surface_dark='#333a47'

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
      background_light='#f0f1f4'
      background_dark='#242632'
      base_dark='#1c1e26'
      surface_dark='#343746'

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

    if [[ "$type" != '' ]]; then
      cp -rf "assets.svg" "assets${theme}${type}.svg"
      sed -i "s/#3c84f7/${theme_color_dark}/g" "assets${theme}${type}.svg"
      sed -i "s/#5b9bf8 /${theme_color_light}/g" "assets${theme}${type}.svg"
      sed -i "s/#F2F2F2/${background_light}/g" "assets${theme}${type}.svg"
      sed -i "s/#2c2c2c/${background_dark}/g" "assets${theme}${type}.svg"
      sed -i "s/#212121/${base_dark}/g" "assets${theme}${type}.svg"
      sed -i "s/#3C3C3C/${surface_dark}/g" "assets${theme}${type}.svg"
    elif [[ "$theme" != '' ]]; then
      cp -rf "assets.svg" "assets${theme}.svg"
      sed -i "s/#3c84f7/${theme_color_dark}/g" "assets${theme}.svg"
      sed -i "s/#5b9bf8/${theme_color_light}/g" "assets${theme}.svg"
    fi
  done
done

echo -e "DONE!"
