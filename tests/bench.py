from pathlib import Path

import bencode2

compat_peers_py = {
    "interval": 3600,
    # 50 peers
    "peers": b"1" * 6 * 50,
    "peers6": b"1" * 18 * 50,
}

compat_peers_encoded = bencode2.bencode(compat_peers_py)


single_file_torrent = (
    Path(__file__)
    .joinpath("../fixtures/ubuntu-22.04.2-desktop-amd64.iso.torrent.bin")
    .resolve()
    .read_bytes()
)


def test_benchmark_encode_compat_peers_bytes_key(benchmark):
    benchmark(
        bencode2.bencode,
        {key.encode(): value for key, value in compat_peers_py.items()},
    )


def test_benchmark_encode_compat_peers_str_key(benchmark):
    benchmark(bencode2.bencode, compat_peers_py)


def test_benchmark_decode_compat_peers(benchmark):
    benchmark(bencode2.bencode, compat_peers_encoded)


def test_benchmark_decode_single_file_torrent(benchmark):
    benchmark(bencode2.bdecode, single_file_torrent)


def test_benchmark_encode_single_file_torrent(benchmark):
    benchmark(bencode2.bdecode, bencode2.bencode(single_file_torrent))
