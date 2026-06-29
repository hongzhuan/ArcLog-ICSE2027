# Ground Truth for zstd-v1.5.2-v1.5.4

## Important Changes

### Application & Tool Layer

- [GT-ZSTD-v1.5.4-0012] cli: Change `zstdless` behavior to align with `zless` (#2909, @binhdvo) (PRs: #2909, #3037, #3059, #3211, #3223, #3242, #3443, #3450; commits: 03cc84f, 17017ac, 3b4e470, 8c85b29, b6fd91b, cee6bec, e653e97)
- [GT-ZSTD-v1.5.4-0014] cli: Keep original files when result is concatenated into a single output with `-o` (#3450, @Cyan4973) (PRs: #3443, #3450; commits: 02434e0, 8c85b29, a82e0aa, b6fd91b, cee6bec)
- [GT-ZSTD-v1.5.4-0092] Improved behavior and error handling of benchmark mode, restricting runs to zstd format only, and returning non-zero error codes and more accurate error messages on failure. (Architecture-related: Benchmark behavior) (PRs: #3463, #3470, #3480; commits: 58e7067, 6740f8f, 9cabd15, af09777)
- [GT-ZSTD-v1.5.4-0124] Fix small file asynchronous IO performance regression, dynamically enable or disable asynchronous IO based on file size. (Architecture-related: asynchronous IO behavior) (PRs: #3474; commits: 79bdb8c)

### Architecture-related Changes

- [GT-ZSTD-v1.5.4-0134] Comprehensively reconstruct Windows CI, upgrade Visual Studio 2022, update msys2 configuration and optimize the test matrix. (Architecture-related: platform compatibility) (PRs: #3374, #3410; commits: 3867c41, 4f7183d)
- [GT-ZSTD-v1.5.4-0136] Add C89 build tests in CI, and fix compilation warnings that are not C89 compatible in the code. (Architecture-related: platform compatibility) (PRs: #3435; commits: ea684c3)

### Core Compression Engine

- [GT-ZSTD-v1.5.4-0001] perf: +20% faster huffman decompression for targets that can't compile x64 assembly (#3449, @terrelln) (PRs: #3449; commits: 8957fef)
- [GT-ZSTD-v1.5.4-0004] pref: +3-11% compression speed for `arm` target (#3199, #3164, #3145, #3141, #3138, @JunHe77 and #3139, #3160, @danlark1) (PRs: #3138, #3139, #3141, #3145, #3160, #3164, #3199, #3219; commits: 05f3f41, 1c8a697, 2491c65, 3b1bd91, 3b915cd, 558cf20, 6b561d2, 778f639, 9166c6a, 97c23cf, b1bbb0e, b944db0, ce52acd, d7249da, e11783b, ec5fdcd)
- [GT-ZSTD-v1.5.4-0006] perf: +10-20% cold dict compression speed by prefetching CDict tables (#3177, @embg) (PRs: #3177; commits: 2a12811, 6bd5ac6, 747e06f, 93b89fb, cb9e341, e9d6fc8)
- [GT-ZSTD-v1.5.4-0008] perf: Small compression ratio improvements in high compression mode (#2983, #3391, @Cyan4973 and #3285, #3302, @daniellerozenblit) (PRs: #2983, #3285, #3302, #3328, #3391; commits: 0d5d571, 1c818e3, 4013319, 482689b, 5434de0, 71921e5, 75cd42a, 834fd07, 8888a2d, 9e1b482, a08fabd, a910489, b347290, c263821, c26f348, c4853e1, ca0135c, db74d04, df714dd, e60cae3, ebba9ff, fa7d9c1)
- [GT-ZSTD-v1.5.4-0009] perf: small speed improvement by better detecting `STATIC_BMI2` for `clang` (#3080, @TocarIP) (PRs: #3080; commits: 7c3d1cb, e8448a3)
- [GT-ZSTD-v1.5.4-0034] api: Streaming decompression detects incorrect header ID sooner (#3175, @Cyan4973) (PRs: #3169, #3175; commits: 91aeade, f5c4ec4)
- [GT-ZSTD-v1.5.4-0057] Add the lib/common/bits.h file to centralize scattered bit operation inline functions here, and update all call points to use unified implementation. (Architectural event: bits.h is added and bit operation is centralized) (PRs: #3045; commits: db2f4a6)
- [GT-ZSTD-v1.5.4-0060] A new maxBlockSize parameter is added, allowing users to control the maximum block size, and supports setting it to 0 to use the default value. (Architecture-related: public API: new maxBlockSize parameter) (PRs: #3418; commits: 06b096d, 1fffcfe, 908e812, fe08137)
- [GT-ZSTD-v1.5.4-0061] Added in-place decompression support, including functions and macros to calculate decompression boundaries to ensure that the output buffer does not overlap the input. (Architecture-related: public API) (PRs: #3421; commits: 5b26619)
- [GT-ZSTD-v1.5.4-0062] Support decompression of empty data blocks, adjust the minimum compression block size from 3 to 2, and fix the relevant verification logic. (Architecture-related: core behavior) (PRs: #3118; commits: 43f21a6)
- [GT-ZSTD-v1.5.4-0066] Fixed slight compression differences in the btlazy2 parser due to sumtype numerical representation dependency, and unified offBase representation. (Architecture-related: core compression module) (PRs: #2965; commits: 03903f5, 7a18d70, f92ec5e)
- [GT-ZSTD-v1.5.4-0069] Move the HufLog macro definition from the public header file to the decompressed internal header file, and fix the return value type conversion of several parameter setting functions. (Architecture-related: public API) (PRs: #3019; commits: 2d154e6, 32a5d95)
- [GT-ZSTD-v1.5.4-0070] Introduce the LitHufLog constant to correctly represent the maximum bit size of compressed literals (11), replace the original default values ​​in many places in the code, and fix several type conversion warnings. (Architecture-related: core compression module) (PRs: #3019; commits: a66e8bb)
- [GT-ZSTD-v1.5.4-0071] Fix the processing logic of zero-valued input in the bit operation inline function, and adjust the conditional compilation details. (Architecture-related: public API) (PRs: #3045; commits: 529cd7b)
- [GT-ZSTD-v1.5.4-0073] Reconstruct the bit operation inline functions in bits.h to implement unified implementation and fix the STATIC_BMI2 check and _BitScanReverse return value calculation errors under MSVC. (Architecture-related: public API) (PRs: #3045; commits: 6994a9f, 7961826, 856c7dc)
- [GT-ZSTD-v1.5.4-0075] Fix the memory read byte order problem of ZSTD_hash4Ptr function on big-endian systems. (Architecture-related: platform compatibility) (PRs: #3227; commits: 1b445c1)
- [GT-ZSTD-v1.5.4-0079] Updated the specification to require 4-streams mode to require at least 6 literals to trigger, and added corresponding checks in the decoder. (Architecture-related: decoding behavior) (PRs: #3398; commits: 6a9c525)
- [GT-ZSTD-v1.5.4-0083] Fixed the data corruption bug caused by incorrect threshold judgment in literal compression, replaced the heuristic judgment by adding actual byte consistency check, and adjusted the minimum literal compression threshold logic. (Architecture-related: public API) (PRs: #3416, #3419; commits: 796699c)
- [GT-ZSTD-v1.5.4-0087] Fixed C89 compatibility warning introduced by side-by-side merging. (Architecture-related: Platform Compatibility) (PRs: #3487; commits: d9280af)
- [GT-ZSTD-v1.5.4-0089] Fixed long offset parsing issue, allocating extra space for long offsets in memory estimation. (Architecture-related: public API) (PRs: #3460; commits: 814f4bf)
- [GT-ZSTD-v1.5.4-0090] Fixed long offset processing logic on 32-bit systems, including multiple scenarios in compression and decompression to avoid data corruption. (Architecture-related: core compression behavior) (PRs: #3460, #3467, #3472; commits: 2bde9fb, 2f74507, cc3e3ac)
- [GT-ZSTD-v1.5.4-0091] Fix buffer overflow and bounds checking issues in multiple legacy format decoders to enhance security and stability. (Architecture-related: backward compatibility) (PRs: #3476; commits: 67d7a65, 7a1a171, 7eb4471, 9419747, b20e4e9, c5bf6b8, cfec005, e04706c)
- [GT-ZSTD-v1.5.4-0093] Fix potential buffer overflow and error propagation issues caused by invalid sequences generated by external matchfinders. (Architecture-related: External matchfinder security) (PRs: #3465; commits: 64052ef)
- [GT-ZSTD-v1.5.4-0116] Replaced multiple Boolean parameters of the Huffman function with flags bit fields, added a new flag to disable the assembly decoder, and deleted unused functions and old suffix functions. (Architecture event: Core_Compression module change) (PRs: #3434; commits: 0cc1b0c, 3291691)
- [GT-ZSTD-v1.5.4-0117] Uniformly use memcpy for unaligned memory access in the legacy code base, and remove other non-memcpy methods. (Architecture-related: platform compatibility) (PRs: #3355; commits: 728e73e)
- [GT-ZSTD-v1.5.4-0119] Removed all unused FSE functions, removing dead code and avoiding stack usage confusion. (Architecture-related: public API) (PRs: #3453, #3462; commits: 423a749)
- [GT-ZSTD-v1.5.4-0122] Changed implementation of unaligned memory access from packed attribute to aligned attribute, improved code generation on ARMv6, ARMv7 and aarch64, and cleaned up duplicate implementation in legacy code. (Architecture-related: Platform compatibility) (PRs: #2881; commits: a78c91a)
- [GT-ZSTD-v1.5.4-0123] Replaced the bit operations in BIT_addBits with the BIT_getLowerBits helper function, and added conditional compilation protection supported by the BMI2 instruction to improve code clarity and reduce data cache pressure. (Architecture-related: platform compatibility) (PRs: #3075; commits: 0178c12)
- [GT-ZSTD-v1.5.4-0128] Fixed the out-of-bounds access problem caused by improper offset calculation in the FSE decompression function, and changed the assertion to conditional judgment in the dictionary training function to eliminate null pointer false positives. (Architecture-related: public API) (PRs: #3020; commits: 8d65f87)
- [GT-ZSTD-v1.5.4-0130] Rewrite the boundary check logic of the old version v0.7, no longer rely on address space overflow, and fix potential security issues discovered by oss-fuzz. (Architecture-related: legacy format backward compatibility) (PRs: #3476; commits: c689310)

### Cross-cutting / Other Architecture-related Changes

- [GT-ZSTD-v1.5.4-0005] perf: +5-30% faster dictionary compression at levels 1-4 (#3086, #3114, #3152, @embg) (PRs: #3086, #3114, #3127, #3152; commits: 2820efe, 3536262, 3620a0a, 518cb83, 64efba4, 6a2e1f7, 7915c11, 809f652, 97aabc4, ac371be, ce6b69f, f6ef143)
- [GT-ZSTD-v1.5.4-0017] cli: Print checksum value for single frame files with `-lv`  (#3332, @Cyan4973) (PRs: #3332; commits: dc39409)
- [GT-ZSTD-v1.5.4-0022] cli: improved help/usage (`-h`,  `-H`) formatting (#3094, @dirkmueller and #3385, @jonpalmisc) (PRs: #3094, #3385, #3487; commits: 2431809, 460780f, 678335c, 7607b96, 7fbe60d, 9c93dd7)
- [GT-ZSTD-v1.5.4-0032] api: Support for in-place decompression (#3432, @terrelln) (PRs: #3432; commits: 0382076, 0d2d460, 1e3eba6, 2ad6855, 3d25502, 5653f96, 7a8c8f3, a5ed28f)
- [GT-ZSTD-v1.5.4-0035] api: Window size resizing optimization for edge case (#3345, @daniellerozenblit) (PRs: #3345; commits: 69ec75f, b0bcbbf)

### High-Level API & Mode Layer

- [GT-ZSTD-v1.5.4-0010] perf: Improved streaming performance when `ZSTD_c_stableInBuffer` is set (#2974, @Cyan4973) (PRs: #2974, #3019, #3026, #3127; commits: 22875ec, 270f9bf, 27d336b, 2b957af, 37b87ad, 4b9d1dd, 5684bae, 7616e39, 8296be4, af3d9c5, b99ece9, bad7f82, c0c5ffa, c1668a0, cbff372, dda4c10, e9dd923, f2d9652)
- [GT-ZSTD-v1.5.4-0031] api: Support for Block-Level Sequence Producer (#3333, @embg) (PRs: #3262, #3333, #3437, #3471; commits: 1613caf, 2a40262, 3f9f568, 3fe5f1f, 7f8189c, aa82998)
- [GT-ZSTD-v1.5.4-0033] api: New  `ZSTD_CCtx_setCParams()`  function, set all parameters defined in a  `ZSTD_compressionParameters`  structure (#3403, @Cyan4973) (PRs: #3395, #3403, #3487; commits: 00c85b2, 481a2e1, 89342d1, b17743e)
- [GT-ZSTD-v1.5.4-0036] api: More accurate error codes for busy-loop scenarios (#3413, #3455, @Cyan4973) (PRs: #3413, #3454, #3455; commits: 423500d, 8b13000, db18a62, efc9ae3)
- [GT-ZSTD-v1.5.4-0037] api: Fix limit overflow in `compressBound` and `decompressBound` (#3362, #3373, Cyan4973) reported by @nigeltao (PRs: #3323, #3362, #3373; commits: 2f4238e, 3a484ef, 45ed0df, 51355e1, 97f63ce, ea24b88)
- [GT-ZSTD-v1.5.4-0038] api: Deprecate several advanced experimental functions: streaming (#3408, @embg), copy (#3196, @mileshu) (PRs: #3128, #3196, #3274, #3408; commits: 434ffe9, 5d8cfa6, 6b233d5, 7e6278a, 962746e, a5655e4, c450f9f)
- [GT-ZSTD-v1.5.4-0041] bug: Fixes for Sequence Compression API (#3023, #3040, @Cyan4973) (PRs: #3023, #3036, #3040; commits: 529a587, 87dcd33, 9a758ce, a0acf9a, cad9f8d, fc2ea97)
- [GT-ZSTD-v1.5.4-0055] misc: Fix `contrib/` seekable format (#3058, @yhoogstrate and #3346, @daniellerozenblit) (PRs: #3058, #3346; commits: 72845eb, aece0f2, f176529)
- [GT-ZSTD-v1.5.4-0059] Two new reserved fields have been added to the ZSTD_frameHeader structure for future expansion. (Architecture-related: public API) (PRs: #3349; commits: e1e82f7)
- [GT-ZSTD-v1.5.4-0072] Fix compilation warnings and C++ compatibility warnings caused by using deprecated APIs in the Linux kernel Zstd compression module, and replace them with recommended APIs to ensure consistent functionality. (Architecture-related: public API) (PRs: #3088; commits: 498ac82, 8ff20c2, e470c94)
- [GT-ZSTD-v1.5.4-0074] Updated zlibWrapper to be compatible with zlib 1.2.12, replacing macros and adding backward compatibility definitions. (Architecture-related: Platform compatibility) (PRs: #3217; commits: 1e09cff)
- [GT-ZSTD-v1.5.4-0076] Adjusted the position of the ZSTD_DEPRECATED macro in the function declaration, and fixed compilation errors in C++14 and C++17 modes under the Clang compiler. (Architecture-related: Platform compatibility) (PRs: #3250, #3273; commits: 5635827)
- [GT-ZSTD-v1.5.4-0077] Optimized the ZSTD_getDictID_fromDDict function to directly read the dictionary ID in the DDict structure, avoiding re-parsing the dictionary buffer, improving efficiency and returning the correct ID when memory is damaged. (Architecture-related: public API) (PRs: #3290; commits: d7841d1)
- [GT-ZSTD-v1.5.4-0078] Fixed the pointer arithmetic problem of NULL + 0 in ZSTD_decompressStream, and improved the stream_decompress fuzzer to support empty buffer input. (Architecture-related: public API) (PRs: #3258, #3351, #3356; commits: 282a955, 69022ad, f31b83f)
- [GT-ZSTD-v1.5.4-0080] Adjusted the position of the deprecation mark so that it is before the static API macro, which solves the compatibility issue when clang compiles C++ code. (Architecture-related: platform compatibility) (PRs: #3400; commits: 48f4aa7)
- [GT-ZSTD-v1.5.4-0081] Fixed the inclusion guard of zdict.h to ensure that static link special symbols can still be exposed correctly when included multiple times. (Architecture-related: public API) (PRs: #3372; commits: 2f7b8d4)
- [GT-ZSTD-v1.5.4-0082] Added invalid external sequence error code, and renamed related errors to externalSequences_invalid. (Architecture-related: public API) (PRs: #3439; commits: 1b65727, 815d1d4)
- [GT-ZSTD-v1.5.4-0084] Fixed multiple issues with the external matcher API: corrected memory space estimation, removed incorrect assertions, prohibited simultaneous use with multiple threads, supported clearing matchers by passing in NULL. (Architecture-related: public API) (PRs: #3433; commits: bce0382)
- [GT-ZSTD-v1.5.4-0085] Limit the upper limit of hashLog and chainLog, ensure that only 32-bit hashes are used, and adjust the window size judgment condition to use memory more accurately. (Architecture-related: public API) (PRs: #3336, #3438; commits: 666944f)
- [GT-ZSTD-v1.5.4-0086] Fixed the problem that when attaching a dictionary in the unbuffered API, the dictionary was not correctly invalidated because non-contiguous segments were not detected. (Architecture-related: public API) (PRs: #3102, #3441; commits: b4467c1)
- [GT-ZSTD-v1.5.4-0088] Fixed build error of zstd seekable format on 32-bit platforms, added explicit size_t type conversion in ZSTD_seekable_decompress function. (Architecture-related: platform compatibility) (PRs: #3452; commits: 63042f1)
- [GT-ZSTD-v1.5.4-0118] Unified the visibility macro name to *_VISIBLE and maintained backward compatibility; added the ZDICTLIB_STATIC_API macro to the zdict library. (Architecture-related: public API) (PRs: #2501, #3359, #3363; commits: 358a237)
- [GT-ZSTD-v1.5.4-0120] Renamed External Matchfinder to Block-Level Sequence Producer, and updated all related function names, type names, parameter names, error codes and test cases. (Architecture-related: public API) (PRs: #3484; commits: ff42ed1)
- [GT-ZSTD-v1.5.4-0121] Added basic functional tests for the maxBlockSize parameter, and corrected related macro definitions and comments. (Architecture-related: public API) (PRs: #3418; commits: 53eb5a7)
- [GT-ZSTD-v1.5.4-0129] Fix the problem of inconsistency between the match length check and the context in the sequence verification logic, and correct the seqStore boundary check to prevent out-of-bounds writes. (Architecture-related: public API) (PRs: #3439; commits: aa385ec)
- [GT-ZSTD-v1.5.4-0131] Fixed the documentation error of ZSTD_estimate* and ZSTD_initCStream(), removed the error warning that the old streaming API is incompatible with advanced parameters and dictionary compression, added a description that ZSTD_initCStream() will clear the dictionary, and noted that the ZSTD_estimate* function does not support external matchfinder API and multi-threading. (Architecture-related: public API documentation correction) (PRs: #3448; commits: 3bfd3be)
- [GT-ZSTD-v1.5.4-0137] Upgrade the version number to v1.5.4 and start preparing for release. (Architecture-related: version and compatibility) (PRs: #3469; commits: 39ceef2)

### Platform Adaptation Layer

- [GT-ZSTD-v1.5.4-0011] cli: Asynchronous I/O for improved cli speed (#2975, #2985, #3021, #3022, @yoniko) (PRs: #2975, #2985, #3021, #3022; commits: 1598e6c, 70df5de, 8ab95f2, cc0657f, df5013b)
- [GT-ZSTD-v1.5.4-0013] cli: Keep original file if `-c` or `--stdout` is given (#3052, @dirkmueller) (PRs: #3052; commits: 3f4f8b0, f229daa)
- [GT-ZSTD-v1.5.4-0021] cli: support for `posix` high resolution timer `clock_gettime()`, for improved benchmark accuracy (#3423, @Cyan4973) (PRs: #3168, #3423, #3447; commits: 2086e73, 638d502, a2ef23d, bbe65d7, bcfb7ad)
- [GT-ZSTD-v1.5.4-0028] cli: Fix decompression memory usage reported by `-vv --long` (#3042, @u1f35c, and #3232, @zengyijing) (PRs: #2968, #3042, #3231, #3232; commits: 3dfcafa, 470eb83, e818fa8, fcef199)
- [GT-ZSTD-v1.5.4-0030] cli: Fix `--adapt` doesn't work when `--no-progress` is also set (#3354, @terrelln) (PRs: #3353, #3354; commits: 15f32ad)
- [GT-ZSTD-v1.5.4-0042] bug: Fix leaking thread handles on Windows (#3147, @animalize) (PRs: #3120, #3147, #3364, #3487; commits: 26f1bf7, 500f02e, 95073b1, 9f346db)
- [GT-ZSTD-v1.5.4-0044] build: Allow user to select legacy level for cmake (#3050, @shadchin) (PRs: #3050; commits: 317bd10, b848c16)
- [GT-ZSTD-v1.5.4-0045] build: Enable legacy support by default in cmake (#3079, @niamster) (PRs: #3079; commits: 03bba1b, db104f6)
- [GT-ZSTD-v1.5.4-0046] build: Meson build script improvements (#3039, #3120, #3122, #3327, #3357, @eli-schwartz and #3276, @neheb) (PRs: #2976, #3039, #3041, #3120, #3122, #3276, #3327, #3357, #3364; commits: 031de3c, 26134b4, 26f1bf7, 4b24ebd, 500f02e, 5b2c6c7, 6548ec7, 66633f9, 6747ba4, 6c3ed93, 7f29c18, 84c0545, 8d522b8, 937e9d3, 9c3e18f, c01582d, ce61cb8, df6eefb, e0ef09d, e873335, ea763f3)
- [GT-ZSTD-v1.5.4-0047] build: Add aarch64 to supported architectures for zstd_trace (#3054, @ooosssososos) (PRs: #3054; commits: 3202c75, fede1d3)
- [GT-ZSTD-v1.5.4-0050] build: Fix Windows issues with Multithreading translation layer (#3364, #3380, @yoniko) and ARM64 target (#3320, @cwoffenden) (PRs: #3120, #3320, #3364, #3375, #3380; commits: 0168914, 0547c3d, 26f1bf7, 3cee69a, 500f02e, 67cd24b, 80cf73f, a8add43, aaa38b2, e9797b5, ec42c92)
- [GT-ZSTD-v1.5.4-0051] build: Fix `cmake` script (#3382, #3392, @terrelln and #3252 @Tachi107 and #3167 @Cyan4973) (PRs: #3135, #3161, #3163, #3167, #3193, #3252, #3259, #3267, #3382, #3392, #3487; commits: 0015308, 14894d6, 1c04514, 2436405, 31a703e, 3367e6d, 651a381, 6640377, 966ac9d, a0b09d0, eceecc5)
- [GT-ZSTD-v1.5.4-0054] misc: Enable Intel CET (#2992, #2994, @hjl-tools) (PRs: #2992, #2994, #3015; commits: 4dfc4ec, 51ab182, 7cf80cb, c7e8315, d6fcdd1)
- [GT-ZSTD-v1.5.4-0058] Added the zstd_common kernel module, changed the kernel-specific code to external mode, and updated the test header file to support GPL symbol export. (Architecture-related: kernel module and GPL export) (PRs: #3292; commits: 330558a)
- [GT-ZSTD-v1.5.4-0063] Added the --trace-file-stat option, which is used to output trace information on stderr for file metadata read and write operations. (Architecture-related: CLI interface) (PRs: #3394; commits: b6e8112)
- [GT-ZSTD-v1.5.4-0067] Refactor the progress bar and summary line display logic, centralize control over display conditions, make the --progress option effective for non-zstd compressors, and fix several edge cases. (Architecture-related: public API) (PRs: #2984; commits: fbff782)
- [GT-ZSTD-v1.5.4-0068] Fixed the issue where the --auto-threads option was ignored when multi-threading was not enabled. Now even if ZSTD_MULTITHREAD is not defined, this option will be parsed normally. (Architecture-related: build and installation methods) (PRs: #3020; commits: 495dcb8)
- [GT-ZSTD-v1.5.4-0132] Add missing util.h header file reference in fileio.h to fix compilation order issue. (Architecture-related: public API) (PRs: #3231; commits: a925362)
- [GT-ZSTD-v1.5.4-0133] Update CircleCI base image to focal, and re-enable aarch64 build. (Architecture-related: platform compatibility) (PRs: #2785, #3367; commits: ef566c8)
- [GT-ZSTD-v1.5.4-0135] Disable custom ASAN/MSAN taint for MinGW builds. (Architecture-related: Platform Compatibility) (PRs: #3240, #3424; commits: f10922a)

## Routine Changes

### Bug Fixes

- [GT-ZSTD-v1.5.4-0023] cli: Fix better handling of bogus numeric values (#3268, @ctkhanhly) (PRs: #3268; commits: 3587877)
- [GT-ZSTD-v1.5.4-0024] cli: Fix input consists of multiple files _and_ `stdin` (#3222, @yoniko) (PRs: #3222; commits: ae46704)
- [GT-ZSTD-v1.5.4-0025] cli: Fix tiny files passthrough (#3215, @cgbur) (PRs: #3215; commits: 2b9fde9)
- [GT-ZSTD-v1.5.4-0026] cli: Fix for `-r` on empty directory (#3027, @brailovich) (PRs: #3027; commits: 4021b78, beb4872, c9072dd)
- [GT-ZSTD-v1.5.4-0027] cli: Fix empty string as argument for `--output-dir-*` (#3220, @embg) (PRs: #3220; commits: 28ceb63, e1873ad, f9f27de)
- [GT-ZSTD-v1.5.4-0029] cli: Fix infinite loop when empty input is passed to trainer (#3081, @terrelln) (PRs: #3081; commits: 4166567, da737c7)
- [GT-ZSTD-v1.5.4-0039] bug: Fix corruption that rarely occurs in 32-bit mode with wlog=25 (#3361, @terrelln) (PRs: #3350, #3361; commits: a91e7ec)
- [GT-ZSTD-v1.5.4-0040] bug: Fix for block-splitter (#3033, @Cyan4973) (PRs: #3033; commits: 5d70ec0, 8df1257)
- [GT-ZSTD-v1.5.4-0043] bug: Fix timing issues with cmake/meson builds (#3166, #3167, #3170, @Cyan4973) (PRs: #3163, #3166, #3167, #3170; commits: 15f3605, 3367e6d, 574ecbb, eb842a2, eceecc5, f15dd64)
- [GT-ZSTD-v1.5.4-0049] build: Fix `ZSTD_LIB_MINIFY` build macro, which now reduces static library size by half (#3366, @terrelln) (PRs: #3066, #3366; commits: 0c42424)
- [GT-ZSTD-v1.5.4-0094] Fix the problem of DiB_shuffle function triggering assertion when the input quantity is 0, and return it directly instead. (PRs: #3007, #3020; commits: 246982e)
- [GT-ZSTD-v1.5.4-0095] The new Huffman depth heuristic algorithm has been removed to make the compression results consistent with those before PR, and the function declaration format has been adjusted. (PRs: #3019; commits: 8b46895)
- [GT-ZSTD-v1.5.4-0096] Fix insufficient compression bounds when using Explicit Block Delimiters, allocate larger buffers for this mode in fuzz tests. (PRs: #3034, #3036, #3103; commits: 637b2d7, 678bfff, d64d5dd)
- [GT-ZSTD-v1.5.4-0097] Added input non-zero check in bit manipulation functions on Win32 platform to avoid static analysis warnings. (PRs: #3045; commits: 00f2acb)
- [GT-ZSTD-v1.5.4-0098] Fix zstreamtest segfault in MALLOC_PERTURB_ environment and change thread pool memory allocation from malloc to calloc. (PRs: #3119, #3288; commits: b7d55cf)
- [GT-ZSTD-v1.5.4-0099] Fix the evaluation order of loop conditions in ZSTD_copySequencesToSeqStoreExplicitBlockDelim to avoid accessing sequence data even after the index is out of bounds. (PRs: #3148; commits: 5081ccb)
- [GT-ZSTD-v1.5.4-0100] Fixed the boundary condition of window overflow correction when loading a large dictionary to avoid triggering assertion failure. (PRs: #3157; commits: 31bd640)
- [GT-ZSTD-v1.5.4-0101] Fix segfault caused by createCompressInstructions being called when doing decompression-only benchmarks. (PRs: #3205; commits: d0c88af)
- [GT-ZSTD-v1.5.4-0102] Fix off-by-one bugs for long literals and matching lengths in superblock mode, and add golden compression tests. (PRs: #3212, #3221; commits: a70ca2b)
- [GT-ZSTD-v1.5.4-0103] Fixed the issue where windowLog was not correctly set to the default value when the --long parameter was not set. (PRs: #3144, #3226; commits: d0dcc9d)
- [GT-ZSTD-v1.5.4-0104] Fix multiple null pointers and undefined behavior issues in ZSTD_decompressStream function. (PRs: #3258, #3263; commits: 0288427, 3d7f9a9, a1d8942, e46b12e, f3ddaad)
- [GT-ZSTD-v1.5.4-0105] Fixed bounds error in buffer overflow check in UTIL_mergeFileNamesTable function, corrected assertion condition from <= to <. (PRs: #3300; commits: 361d869)
- [GT-ZSTD-v1.5.4-0106] Supports decompression of compressed blocks with a size of exactly ZSTD_BLOCKSIZE_MAX, and relaxes the compression block size check conditions. (PRs: #3399; commits: ea2895c)
- [GT-ZSTD-v1.5.4-0107] Fixed missing brackets in macro definition and corrected BIT_highbit32 call to ZSTD_highbit32. (PRs: #3301, #3365; commits: ee6475c)
- [GT-ZSTD-v1.5.4-0108] Fixed an issue where parameters in macro definitions were not bracketed, and fixed a wrong assertion in the ZSTD_fracWeight function. (PRs: #3248; commits: d07e72b)
- [GT-ZSTD-v1.5.4-0109] Fixed type conversion warning, changed ZSTD_fCost function parameter type from U32 to int, and adjusted related assertions. (PRs: #3487; commits: 71dbe8f)
- [GT-ZSTD-v1.5.4-0110] Fixed parsing issue with maxBlockSize parameter in estimation function. (PRs: #3418; commits: 8353a4b)
- [GT-ZSTD-v1.5.4-0111] Fixed bounds check on sequence index in ZSTD_copySequencesToSeqStoreNoBlockDelim, only incrementing index when splitting sequence non-finally. (PRs: #3447; commits: 7d600c6)
- [GT-ZSTD-v1.5.4-0112] Fixed the bug of redzone depoisoning. Now only the expected buffer is depoisoned, and subsequent redzone depoisoning is no longer detoxified. (PRs: #3451; commits: 1d636b4)
- [GT-ZSTD-v1.5.4-0113] Fixed a bug where the --row-match-finder and --no-row-match-finder command line options behaved reversely, now the options correctly enable or disable the row match finder. (PRs: #3457; commits: 6422d1d)
- [GT-ZSTD-v1.5.4-0114] Fixed the bug of input boundary checking in the fast C decoder, and changed the break of the inner loop to goto _out to correctly jump out of the outer loop. (PRs: #3459; commits: bda947e)
- [GT-ZSTD-v1.5.4-0115] Fix the incorrect return value of ZSTD_getOffsetInfo() when nbSeq is 0 because the offset table is not initialized. (PRs: #3473; commits: 71a0259)
- [GT-ZSTD-v1.5.4-0145] Fixed bugs found in other projects (commits: 5fd6dda)

### Build and CI

- [GT-ZSTD-v1.5.4-0048] build: support AIX architecture (#3219, @qiongsiwu) (PRs: #3139, #3219; commits: 9166c6a, b1bbb0e)
- [GT-ZSTD-v1.5.4-0138] Fixed build errors caused by incompatible test compilation options under MSVC. (PRs: #3180; commits: cd9d0a7)
- [GT-ZSTD-v1.5.4-0139] Fix the return type checking error in the Meson build script and solve the problem that zstd cannot be built. (PRs: #3368; commits: e8401e9)
- [GT-ZSTD-v1.5.4-0140] escape glob pattern special characters in subject string before generating search patterns in combine.sh list_has_item (commits: 60fcc36)
- [GT-ZSTD-v1.5.4-0142] Unbreak FreeBSD CI (commits: 83049cb)
- [GT-ZSTD-v1.5.4-0143] Suggestion from code review (commits: 786263e)
- [GT-ZSTD-v1.5.4-0144] Python style change (commits: 566ebce)
- [GT-ZSTD-v1.5.4-0146] Feature parity with original shell script; needs further testing (commits: 8f1e51f)

### Documentation

- [GT-ZSTD-v1.5.4-0052] doc: Updated man page, providing more details for `--train` mode (#3112, @Cyan4973) (PRs: #3111, #3112, #3487; commits: 0df2fd6, 27bf96e, f1faab6)
- [GT-ZSTD-v1.5.4-0053] doc: Add decompressor errata document (#3092, @terrelln) (PRs: #3092; commits: 696fa25, 6a8fba9)
- [GT-ZSTD-v1.5.4-0147] Work-in-progress; annotated types, added docs, parsed and resolved excluded files (commits: 829ac2e)

### New Features

- [GT-ZSTD-v1.5.4-0015] cli: Preserve Permissions and Ownership of regular files (#3432, @felixhandte) (PRs: #3432; commits: 0382076, 0d2d460, 1e3eba6, 2ad6855, 3d25502, 5653f96, 7a8c8f3, a5ed28f)
- [GT-ZSTD-v1.5.4-0016] cli: Print zlib/lz4/lzma library versions with `-vv` (#3030, @terrelln) (PRs: #3030; commits: 85a1325, e60eba5)
- [GT-ZSTD-v1.5.4-0018] cli: Print `dictID` when present with `-lv` (#3184, @htnhan) (PRs: #3184; commits: 02ef78b, cc8c984, d7eb829)
- [GT-ZSTD-v1.5.4-0019] cli: when `stderr` is *not* the console, disable status updates, but preserve final summary (#3458, @Cyan4973) (PRs: #3458; commits: 82ca008, 88b7088)
- [GT-ZSTD-v1.5.4-0020] cli: support `--best` and `--no-name` in `gzip` compatibility mode (#3059, @dirkmueller) (PRs: #3037, #3059; commits: 8814aa5, e653e97)
- [GT-ZSTD-v1.5.4-0064] Added --fake-stdin-is-console, --fake-stdout-is-console and --fake-stderr-is-console command line options for simulating the console in tests. (PRs: #2984; commits: e58a39f)
- [GT-ZSTD-v1.5.4-0065] Support high-level API to make forceCopy/forceAttach functions work properly. (PRs: #3161; commits: f7ebbcd)

### Performance

- [GT-ZSTD-v1.5.4-0002] perf: up to +10% faster streaming compression at levels 1-2 (#3114, @embg) (PRs: #3114, #3127; commits: 2820efe, 3536262, 3620a0a, 518cb83, 6a2e1f7, 7915c11, 809f652, 97aabc4, ac371be, ce6b69f)
- [GT-ZSTD-v1.5.4-0003] perf: +4-13% for levels 5-12 by optimizing function generation (#3295, @terrelln) (PRs: #2828, #3275, #3295; commits: dcc7228)
- [GT-ZSTD-v1.5.4-0007] perf: +1% faster compression by removing a branch in ZSTD_fast_noDict (#3129, @felixhandte) (PRs: #3129, #3229, #3230, #3487; commits: 040986a, 1c847e2, 1dd046a, 8af64f4, cd1f582, ecd7601)
- [GT-ZSTD-v1.5.4-0056] misc: Improve speed of the one-file library generator (#3241, @wahern and #3005, @cwoffenden) (PRs: #3005, #3108, #3241; commits: 155d6a5, 3f181b6, 7d90f0b, b27356f, dd7d29a, f133bc8)
- [GT-ZSTD-v1.5.4-0125] The heuristic algorithm for Huffman tree depth selection has been improved to avoid over-adjustment in specific corner situations, thereby improving the compression ratio. (PRs: #3019; commits: 51da2d2)
- [GT-ZSTD-v1.5.4-0126] Changed the threshold for automatic tree depth adjustment from maximum to default to improve compression ratio in certain cases. (PRs: #3019; commits: 5db717a)
- [GT-ZSTD-v1.5.4-0127] Removed expensive assertions in --rsyncable hot loops to improve performance, and added equivalent assertions at the beginning and end of the loop to maintain coverage. (PRs: #3150, #3154; commits: 7c05b9a)
- [GT-ZSTD-v1.5.4-0141] restore combine.sh bash performance while still sticking to POSIX (commits: cca3544)
- [GT-ZSTD-v1.5.4-0148] Using faster Python script to amalgamate (commits: 7e50d1e)
