#! /usr/bin/env bash

for theme in '' '-Purple' '-Pink' '-Red' '-Orange' '-Yellow' '-Green' '-Teal' '-Grey'; do
  for color in '' '-Dark'; do
    for type in '' '-Nord' '-Dracula'; do
      if [[ "$color" == '' ]]; then
        case "$theme" in
          '')
            theme_color='#8caaee'
            ;;
          -Purple)
            theme_color='#ca9ee6'
            ;;
          -Pink)
            theme_color='#f4b8e4'
            ;;
          -Red)
            theme_color='#e78284'
            ;;
          -Orange)
            theme_color='#ef9f76'
            ;;
          -Yellow)
            theme_color='#e5c890'
            ;;
          -Green)
            theme_color='#a6d189'
            ;;
          -Teal)
            theme_color='#81c8be'
            ;;
          -Grey)
            theme_color='#45475a'
            ;;
        esac

        if [[ "$type" == '-Nord' ]]; then
          background_color='#f8fafc'

          case "$theme" in
            '')
              theme_color='#5e81ac'
              ;;
            -Purple)
              theme_color='#b57daa'
              ;;
            -Pink)
              theme_color='#cd7092'
              ;;
            -Red)
              theme_color='#c35b65'
              ;;
            -Orange)
              theme_color='#d0846c'
              ;;
            -Yellow)
              theme_color='#e4b558'
              ;;
            -Green)
              theme_color='#82ac5d'
              ;;
            -Teal)
              theme_color='#83b9b8'
              ;;
            -Grey)
              theme_color='#3a4150'
              ;;
          esac
        fi

        if [[ "$type" == '-Dracula' ]]; then
          background_color='#f9f9fb'

          case "$theme" in
            '')
              theme_color='#a679ec'
              ;;
            -Purple)
              theme_color='#a679ec'
              ;;
            -Pink)
              theme_color='#f04cab'
              ;;
            -Red)
              theme_color='#f44d4d'
              ;;
            -Orange)
              theme_color='#f8a854'
              ;;
            -Yellow)
              theme_color='#e8f467'
              ;;
            -Green)
              theme_color='#4be772'
              ;;
            -Teal)
              theme_color='#20eed9'
              ;;
            -Grey)
              theme_color='#3c3f51'
              ;;
          esac
        fi
      else
        case "$theme" in
          '')
            theme_color='#1e66f5'
            ;;
          -Purple)
            theme_color='#8839ef'
            ;;
          -Pink)
            theme_color='#ea76cb'
            ;;
          -Red)
            theme_color='#d20f39'
            ;;
          -Orange)
            theme_color='#fe640b'
            ;;
          -Yellow)
            theme_color='#df8e1d'
            ;;
          -Green)
            theme_color='#40a02b'
            ;;
          -Teal)
            theme_color='#179299'
            ;;
          -Grey)
            theme_color='#ccd0da'
            ;;
        esac

        if [[ "$type" == '-Nord' ]]; then
          background_color='#242932'

          case "$theme" in
            '')
              theme_color='#89a3c2'
              ;;
            -Purple)
              theme_color='#c89dbf'
              ;;
            -Pink)
              theme_color='#dc98b1'
              ;;
            -Red)
              theme_color='#d4878f'
              ;;
            -Orange)
              theme_color='#dca493'
              ;;
            -Yellow)
              theme_color='#eac985'
              ;;
            -Green)
              theme_color='#a0c082'
              ;;
            -Teal)
              theme_color='#83b9b8'
              ;;
            -Grey)
              theme_color='#d9dce3'
              ;;
          esac
        fi

        if [[ "$type" == '-Dracula' ]]; then
          background_color='#242632'

          case "$theme" in
            '')
              theme_color='#bd93f9'
              ;;
            -Purple)
              theme_color='#bd93f9'
              ;;
            -Pink)
              theme_color='#ff79c6'
              ;;
            -Red)
              theme_color='#ff5555'
              ;;
            -Orange)
              theme_color='#ffb86c'
              ;;
            -Yellow)
              theme_color='#f1fa8c'
              ;;
            -Green)
              theme_color='#50fa7b'
              ;;
            -Teal)
              theme_color='#50fae9'
              ;;
            -Grey)
              theme_color='#d9dae3'
              ;;
          esac
        fi
      fi

      if [[ "$type" != '' ]]; then
        cp -r "assets${color}.svg" "assets${theme}${color}${type}.svg"
        # cp -r "assets-common${color}.svg" "assets-common${color}${type}.svg"
        if [[ "$color" == '' ]]; then
          sed -i "s/#3c84f7/${theme_color}/g" "assets${theme}${color}${type}.svg"
          # sed -i "s/#FAFAFA/${background_color}/g" "assets-common${color}${type}.svg"
        else
          sed -i "s/#5b9bf8/${theme_color}/g" "assets${theme}${color}${type}.svg"
          # sed -i "s/#2C2C2C/${background_color}/g" "assets-common${color}${type}.svg"
        fi
      elif [[ "$theme" != '' ]]; then
        cp -r "assets${color}.svg" "assets${theme}${color}.svg"
        if [[ "$color" == '' ]]; then
          sed -i "s/#3c84f7/${theme_color}/g" "assets${theme}${color}.svg"
        else
          sed -i "s/#5b9bf8/${theme_color}/g" "assets${theme}${color}.svg"
        fi
      fi

    done
  done
done

echo -e "DONE!"
