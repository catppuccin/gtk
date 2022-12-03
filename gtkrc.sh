make_gtkrc() {
  local dest="${1}"
  local name="${2}"
  local theme="${3}"
  local color="${4}"
  local size="${5}"
  local ctype="${6}"
  local window="${7}"

  [[ "${color}" == '-Light' ]] && local ELSE_LIGHT="${color}"
  [[ "${color}" == '-Dark' ]] && local ELSE_DARK="${color}"

  local GTKRC_DIR="${SRC_DIR}/main/gtk-2.0"
  local THEME_DIR="${1}/${2}${3}${4}${5}${6}"

  if [[ "${color}" != '-Dark' ]]; then
    case "$theme" in
      '')
        theme_color='#3c84f7'
        ;;
      -Purple)
        theme_color='#AB47BC'
        ;;
      -Pink)
        theme_color='#EC407A'
        ;;
      -Red)
        theme_color='#E53935'
        ;;
      -Orange)
        theme_color='#F57C00'
        ;;
      -Yellow)
        theme_color='#FBC02D'
        ;;
      -Green)
        theme_color='#4CAF50'
        ;;
      -Teal)
        theme_color='#009688'
        ;;
      -Grey)
        theme_color='#464646'
        ;;
    esac

    if [[ "$ctype" == '-Nord' ]]; then
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

    if [[ "$ctype" == '-Dracula' ]]; then
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

    if [[ "$ctype" == '-Catppuccin-mocha' ]]; then
      case "$theme" in
        '')
          theme_color='#cba6f7'
          ;;
        -Purple)
          theme_color='#cba6f7'
          ;;
        -Pink)
          theme_color='#f5c2e7'
          ;;
        -Red)
          theme_color='#f38ba8'
          ;;
        -Orange)
          theme_color='#fab387'
          ;;
        -Yellow)
          theme_color='#f9e2af'
          ;;
        -Green)
          theme_color='#a6e3a1'
          ;;
        -Teal)
          theme_color='#94e2d5'
          ;;
        -Grey)
          theme_color='#a6adc8'
          ;;
      esac
    fi
    if [[ "$ctype" == '-Catppuccin-macchiato' ]]; then
      case "$theme" in
        '')
          theme_color='#c6a0f6'
          ;;
        -Purple)
          theme_color='#c6a0f6'
          ;;
        -Pink)
          theme_color='#f5bde6'
          ;;
        -Red)
          theme_color='#ed8796'
          ;;
        -Orange)
          theme_color='#f5a97f'
          ;;
        -Yellow)
          theme_color='#eed49f'
          ;;
        -Green)
          theme_color='#a6da95'
          ;;
        -Teal)
          theme_color='#8bd5ca'
          ;;
        -Grey)
          theme_color='#a5adcb'
          ;;
      esac
    fi

    if [[ "$ctype" == '-Catppuccin-frappe' ]]; then
      case "$theme" in
        '')
          theme_color='#ca9ee6'
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
          theme_color='#a5adce'
          ;;
      esac
    fi
     if [[ "$ctype" == '-Catppuccin-latte' ]]; then
      case "$theme" in
        '')
          theme_color='#8839ef'
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
          theme_color='#6c6f85'
          ;;
      esac
    fi

  else
    case "$theme" in
      '')
        theme_color='#5b9bf8'
        ;;
      -Purple)
        theme_color='#BA68C8'
        ;;
      -Pink)
        theme_color='#F06292'
        ;;
      -Red)
        theme_color='#F44336'
        ;;
      -Orange)
        theme_color='#FB8C00'
        ;;
      -Yellow)
        theme_color='#FFD600'
        ;;
      -Green)
        theme_color='#66BB6A'
        ;;
      -Teal)
        theme_color='#4DB6AC'
        ;;
      -Grey)
        theme_color='#DDDDDD'
        ;;
    esac

    if [[ "$ctype" == '-Nord' ]]; then
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

    if [[ "$ctype" == '-Dracula' ]]; then
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

  if [[ "$blackness" == 'true' ]]; then
    case "$ctype" in
      '')
        background_light='#FFFFFF'
        background_dark='#0F0F0F'
        background_darker='#121212'
        background_alt='#212121'
        titlebar_light='#F2F2F2'
        titlebar_dark='#030303'
        ;;
      -Nord)
        background_light='#f8fafc'
        background_dark='#0d0e11'
        background_darker='#0f1115'
        background_alt='#1c1f26'
        titlebar_light='#f0f1f4'
        titlebar_dark='#020203'
        ;;
      -Dracula)
        background_light='#f9f9fb'
        background_dark='#0d0d11'
        background_darker='#0f1015'
        background_alt='#1c1e26'
        titlebar_light='#f0f1f4'
        titlebar_dark='#020203'
        ;;
    esac
  else
    case "$ctype" in
      '')
        background_light='#FFFFFF'
        background_dark='#2C2C2C'
        background_darker='#3C3C3C'
        background_alt='#464646'
        titlebar_light='#F2F2F2'
        titlebar_dark='#242424'
        ;;
      -Nord)
        background_light='#f8fafc'
        background_dark='#242932'
        background_darker='#333a47'
        background_alt='#3a4150'
        titlebar_light='#f0f1f4'
        titlebar_dark='#1e222a'
        ;;
      -Dracula)
        background_light='#f9f9fb'
        background_dark='#242632'
        background_darker='#343746'
        background_alt='#3c3f51'
        titlebar_light='#f0f1f4'
        titlebar_dark='#1f2029'
        ;;
      -Catppuccin-mocha)
        background_light='#cdd6f4'
        background_dark='#1e1e2e'
        background_darker='#181825'
        background_alt='#6c7086'
        titlebar_light='#cdd6f4'
        titlebar_dark='#1e1e2e'
        ;;
      -Catppuccin-macchiato)
        background_light='#cad3f5'
        background_dark='#24273a'
        background_darker='#1e2030'
        background_alt='#6e738d'
        titlebar_light='#cad3f5'
        titlebar_dark='#24273a'
        ;;
      -Catppuccin-frappe)
        background_light='#c6d0f5'
        background_dark='#303446'
        background_darker='#292c3c'
        background_alt='#737994'
        titlebar_light='#c6d0f5'
        titlebar_dark='#303446'
        ;;
    -Catppuccin-latte)
        background_light='#eff1f5' # Latte base 
        background_dark='#5c5f77' # Latte subtext1 
        background_darker='#4c4f69' # Latte text
        background_alt='#9ca0b0' # Latte overlay0. Don't know where this is used. 
        titlebar_light='#dce0e8' # Latte crust
        titlebar_dark='#4c4f69' # Latte text
    esac
  fi

  cp -r "${GTKRC_DIR}/gtkrc${ELSE_DARK:-}-default"                              "${THEME_DIR}/gtk-2.0/gtkrc"
  sed -i "s/#FFFFFF/${background_light}/g"                                      "${THEME_DIR}/gtk-2.0/gtkrc"
  sed -i "s/#2C2C2C/${background_dark}/g"                                       "${THEME_DIR}/gtk-2.0/gtkrc"
  sed -i "s/#464646/${background_alt}/g"                                        "${THEME_DIR}/gtk-2.0/gtkrc"

  if [[ "${color}" == '-Dark' ]]; then
    sed -i "s/#5b9bf8/${theme_color}/g"                                         "${THEME_DIR}/gtk-2.0/gtkrc"
    sed -i "s/#3C3C3C/${background_darker}/g"                                   "${THEME_DIR}/gtk-2.0/gtkrc"
    sed -i "s/#242424/${titlebar_dark}/g"                                       "${THEME_DIR}/gtk-2.0/gtkrc"
  else
    sed -i "s/#3c84f7/${theme_color}/g"                                         "${THEME_DIR}/gtk-2.0/gtkrc"
    sed -i "s/#F2F2F2/${titlebar_light}/g"                                      "${THEME_DIR}/gtk-2.0/gtkrc"
  fi
}
