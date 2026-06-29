# Ground Truth for zstd-v1.5.1-v1.5.2

## Important Changes

### Application & Tool Layer

- [GT-ZSTD-v1.5.2-0005] Fixed an issue where the progress bar was incorrectly printed when using the -q option to decompress and specify an output file. (Architecture-related: CLI behavior) (PRs: #2967, #2982; commits: 308a11b)
- [GT-ZSTD-v1.5.2-0016] By inlining the xxHash header file, the dependence on the xxHash dynamic library symbol is removed, allowing the zstd binary to be dynamically linked to the library. (Architecture-related: build and installation methods) (PRs: #2977; commits: 4bd96a6)

### Architecture-related Changes

- [GT-ZSTD-v1.5.2-0012] Fix the problem of MSVC compilation failure in Meson build, conditionalize assembly source files, enable it only for GCC and Clang compilers, and explicitly disable assembly support for non-clang/gcc compilers. (Architecture-related: build and installation mode) (PRs: #2951, #2972; commits: 29e44bc, c4f5116)
- [GT-ZSTD-v1.5.2-0013] Fix the problem of MSVC compilation failure in CMake build, correctly exclude assembly source files, and add compilation options for MSVC to explicitly disable assembly. (Architecture-related: build and installation mode) (PRs: #2957; commits: 148ff15, df5ad5a)
- [GT-ZSTD-v1.5.2-0014] Fixed the issue where the zstd static library output name is incorrect when using the Clang compiler in the MINGW environment. (Architecture-related: build and installation methods) (PRs: #2947; commits: 14a0eaf)
- [GT-ZSTD-v1.5.2-0017] Fix the build system, change the compilation of assembly files from using CFLAGS to using ASFLAGS, and add the -Wa, --noexecstack flag. (Architecture-related: build and installation methods) (PRs: #3006, #3009; commits: 8ea3d57)

### Core Library Layer

- [GT-ZSTD-v1.5.2-0003] doc: Clarify Licensing (@terrelln, #2981) (PRs: #2981, #3000; commits: 5f2c3d9, 9b6dfed)
- [GT-ZSTD-v1.5.2-0004] Fix the POOL_sizeof function prototype and add const qualifier to its parameters. (Architecture-related: public API) (PRs: #2995; commits: 6211bfe, b1978d6)
- [GT-ZSTD-v1.5.2-0009] Hide x86-64 internal assembly functions so that they are no longer exposed in the dynamic symbol table. (Architecture-related: public API) (PRs: #2990, #2993; commits: 568c69a)
- [GT-ZSTD-v1.5.2-0015] In Linux kernel scenarios, replace memcpy calls with ZSTD_memcpy to ensure correct function redirection. (Architecture-related: platform compatibility) (PRs: #2962; commits: ad7c9fc)
- [GT-ZSTD-v1.5.2-0018] The version number has been upgraded to 1.5.2, and the version macro definition in the header file has been updated. (Architecture-related: version and compatibility) (PRs: #2987; commits: 46ad937)

### Cross-cutting / Other Architecture-related Changes

- [GT-ZSTD-v1.5.2-0002] build: Build Zstd with `noexecstack` on All Architectures (@felixhandte, #2964) (PRs: #2964; commits: 4620ce6, 7e67951, ff5d1da)

## Routine Changes

### Bug Fixes

- [GT-ZSTD-v1.5.2-0006] Fix regression test assertions to ensure offset codes for candidate matches are calculated using the STORE_OFFSET macro only in valid cases. (PRs: #2962; commits: 435f5a2)
- [GT-ZSTD-v1.5.2-0007] Fixed the out-of-bounds access problem in the optimal parser caused by the literal length exceeding the format representation range. (PRs: #2980; commits: 4d8a213)
- [GT-ZSTD-v1.5.2-0008] Fixed an issue where timestamps were incorrectly updated when the output target was standard output. (PRs: #2998; commits: 57a86d9)
- [GT-ZSTD-v1.5.2-0019] [license] Fix license header of huf_decompress_amd64.S (commits: c7b03c2)

### Build and CI

- [GT-ZSTD-v1.5.2-0020] Update the Swift Package Definition to Reflect Move (commits: 1778222)

### Functional Changes / Refactorings

- [GT-ZSTD-v1.5.2-0010] The STORE_OFFSET() and STORE_REPCODE() macros are introduced to abstract the offset and repetition code numerical representation passed to ZSTD_storeSeq(), and update multiple call points, while the behavior remains unchanged. (PRs: #2954, #2962; commits: 1aed962, 2068889, 321583c, 92a08ee, a34ccad, b7630a4, b77fcac, e909fa6)
- [GT-ZSTD-v1.5.2-0011] Split the repeated offset update function into updateRep() that updates in place and newRep() that returns a new structure, clarifying the two behaviors. (PRs: #2962; commits: 6fa640e)

### Performance

- [GT-ZSTD-v1.5.2-0001] perf: Regain Minimal memset()-ing During Reuse of Compression Contexts (@Cyan4973, #2969) (PRs: #2966, #2969; commits: 3c2c3fb, 41ad733, 8c53e52)
