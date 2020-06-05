a_var="a value"

a_func() {
    local arg="$1"; shift
    echo "a_func: arg=$arg"
}
