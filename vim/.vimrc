set number
set tabstop=4
set shiftwidth=4
set softtabstop=4
set expandtab

" set mouse=a

syntax enable

if &term =~ '256color'

    " The following two lines solve the BCE issue described here: https://sunaku.github.io/vim-256color-bce.html
    set term=screen-256color
    set t_ut=

    set background=dark

    " Be sure to store your `<theme>.vim` files in ~/.vim/colors/
    " colorscheme gruvbox
    colorscheme monokai
    "colorscheme solarized

endif
