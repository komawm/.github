#!/usr/bin/env bash
# Source explicitly from Bash; this does not edit shell or global tool config.

if [[ "${BASH_SOURCE[0]}" == "$0" ]]; then
    printf '%s\n' 'Source this file from Bash: source .github/scripts/env.sh' >&2
    exit 1
fi

_koma_env_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd -P)"
export KOMA_WORKSPACE="$_koma_env_root"

# Select only an actually installed toolchain matching the product's single pin.
if [[ -f "$_koma_env_root/koma/rust-toolchain.toml" ]]; then
    _koma_env_channel="$(python3 -c 'import re,sys,tomllib; channel=tomllib.load(open(sys.argv[1],"rb"))["toolchain"]["channel"]; assert re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+",channel); print(channel)' "$_koma_env_root/koma/rust-toolchain.toml")" || return 1
    for _koma_env_toolchain in "$_koma_env_root"/.targets/rustup/toolchains/"$_koma_env_channel"-*; do
        if [[ -d "$_koma_env_toolchain" ]]; then
            export RUSTUP_HOME="$_koma_env_root/.targets/rustup"
            break
        fi
    done
fi

# This local cache is created explicitly by workspace setup, never copied from
# the user's global credentials or config. No directory is created by sourcing.
if [[ -d "$_koma_env_root/.targets/cargo" ]]; then
    export CARGO_HOME="$_koma_env_root/.targets/cargo"
fi

unset _koma_env_root _koma_env_toolchain _koma_env_channel
