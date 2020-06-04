#   XDG environment variable setup and search

set_xdg_dirs() {
    export XDG_DATA_HOME=${XDG_DATA_HOME:-$HOME/.local/share/}
    export XDG_DATA_DIRS=${XDG_DATA_DIRS:-/usr/local/share/:/usr/share/}
    export XDG_CONFIG_HOME=${XDG_CONFIG_HOME:-$HOME/.config/}
    export XDG_CONFIG_DIRS=${XDG_CONFIG_DIRS:-/etc/xdg }
    export XDG_CACHE_HOME=${XDG_CACHE_HOME:-$HOME/.cache}
}

set_xdg_runtime_dir() {
    [[ -z $XDG_RUNTIME_DIR ]] || return 0
    [[ -n $UID ]] || return 1
    local tmp=${TMPDIR:-/tmp}
    local XDG_RUNTIME_DIR=${XDG_RUNTIME_DIR:-$TMPDIR/xdgrun-$UID}
    mkdir -m 0700 -p "$XDG_RUNTIME_DIR" || return $?
    #   Ensures user owns the dir, since it will fail if he doesn't.
    chmod 0700 "$XDG_RUNTIME_DIR" || return $?
    export XDG_RUNTIME_DIR
    return 0
}

xdg_search() {
    local type="$1"; shift      # CONFIG or DATA
    local path="$2"; shift
    # XXX fill this in to search for $path in the list of paths
    # created from $XDG_${type}_HOME:$XDG_${type}_DIRS.
}
