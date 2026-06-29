# Ground Truth for zstd-v1.5.6-v1.5.7

## Important Changes

### Architecture-related Changes

- [GT-ZSTD-v1.5.7-0026] Enabled weak symbol support on RISC-V architecture. (Architecture-related: Platform compatibility) (PRs: #4069, #4114; commits: 6dbd49b)
- [GT-ZSTD-v1.5.7-0028] Enabled x86_64 assembly support on Windows platforms. (Architecture-related: Platform compatibility) (PRs: #4246; commits: 46e17b8)
- [GT-ZSTD-v1.5.7-0033] Fixed the build problem when using clang 16 and above on Windows x86, and adjusted the conditional judgment of CPUID detection. (Architecture-related: platform compatibility) (PRs: #3998; commits: 72c16b1)
- [GT-ZSTD-v1.5.7-0037] Fixed an issue caused by the unavailability of register %rbx when using clang in 32-bit mode, by adding a check for 64-bit mode to disable the relevant code paths in 32-bit mode. (Architecture-related: platform compatibility) (PRs: #4118; commits: 5e0a83e)
- [GT-ZSTD-v1.5.7-0059] Replace C11's alignas with the _Alignas keyword to eliminate dependence on header files. (Architecture-related: Platform compatibility) (PRs: #4286; commits: bcf404c)
- [GT-ZSTD-v1.5.7-0063] Adjusted the header file inclusion location and extern "C" block structure in debug.h and huf.h, and fixed C++ compilation compatibility issues. (Architecture-related: public API) (PRs: #4218; commits: 63acf9a)
- [GT-ZSTD-v1.5.7-0064] Re-added extern "C" block in xxhash.h to support C++ compilation. (Architecture-related: public API) (PRs: #4218; commits: 8f49db5)
- [GT-ZSTD-v1.5.7-0065] Fixed the problem that the resource compiler include directory path in the CMake build script was not quoted, ensuring that the path can be quoted correctly even if it contains spaces. (Architecture-related: build and installation methods) (PRs: #4268, #4269; commits: 6cd4204, be1bf24)
- [GT-ZSTD-v1.5.7-0066] A variant pkg-config file is provided for the multi-threaded static library so that it correctly contains the -pthread link and compile flag. (Architecture-related: pkg-config configuration) (PRs: #4020; commits: f1f1ae3)
- [GT-ZSTD-v1.5.7-0067] Fixed an issue with $filter parameters being in the wrong order, and improved recognition of MSYS/Cygwin environments. (Architecture-related: Platform compatibility) (PRs: #4067; commits: f19c982)
- [GT-ZSTD-v1.5.7-0068] Adjusted the libzstd dependency management in the Meson build, separated internal dependencies from public dependencies, avoided name conflicts caused by private header file export, and fixed the construction of contrib and tests. (Architecture-related: build and installation methods) (PRs: #4153; commits: ccc02a9, d2d49a1)
- [GT-ZSTD-v1.5.7-0069] Added compile-time macro support for old libc that does not support fseeko/ftello. (Architecture-related: platform compatibility) (PRs: #4229; commits: 54c3d99)
- [GT-ZSTD-v1.5.7-0070] Added noexecstack compilation and linking flags to GCC/Clang, and added alignment attribute macro detection to the ClangCL compiler. (Architecture-related: Platform compatibility) (PRs: #4284, #4286; commits: 54e9d46, 7b856e3)
- [GT-ZSTD-v1.5.7-0071] Removed x32 ABI test task, and updated ARM64 test configuration, including QEMU system package and CFLAGS parameters. (Architecture-related: platform compatibility) (PRs: #4293; commits: 0b8119f, 2b7c661, 75bcae1, fc1baf3)
- [GT-ZSTD-v1.5.7-0076] Adjusted the position and scope of extern "C" blocks in multiple header files to improve C++ compatibility; removed extern "C" blocks from bitstream.h and fse.h to simplify header file structure. (Architecture-related: C++ compatibility) (PRs: #4218; commits: 07ffcc6, 5222dd8, 58a7f4b, a7bb6d6, c727d5c, d0d5ce4, d51e607, f25b9f1, fa5bfb6, fc726da)

### Core Compression Engine

- [GT-ZSTD-v1.5.7-0002] api: new method `ZSTD_compressSequencesAndLiterals()` (#4217, #4232) (PRs: #3991, #4136, #4214, #4217, #4218, #4228, #4229, #4232, #4250, #4258, #4287; commits: 0165eeb, 03d95f9, 0442e43, 047db4f, 04a2a02, 08edecb, 09964c6, 0a54f6f, 0a5c080, 0b013b2, 10b9d81, 125f052, 12c47d3, 13b9296, 14a21e4, 1ac79ba, 1c8f5b0, 1f6d681, 2503b64, 25bef24, 27d7940, 2949252, 2f3ee8b, 30671d7, 31b5ef2, 33747e2, 41c667c, 477a010, 47cbfc8, 4aaf9ce, 4c097b4, 4ef9d7d, 50ca998, 5164d44, 522adc3, 52a9bc6, 5359d16, 56cfb78, 57a4554, 590c224, 5df80ac, 61ac831, 6b046f5, 6f8e6f3, 72ce56b, 76445bb, 76dd3a9, 788926f, 7b294ca, 7bad787, 81a5e5d, 87f0a4f, 8867204, 894ea31, 8ab0409, 8b7e1b7, 8bff69a, 8d4506b, 8d62164, 8eb2587, 95ad9e4, 9671813, a00f45a, a0872a8, a224572, a288751, a80f55f, aa2cdf9, ab0f179, ac05ea8, ad023b3, b339eff, b4a40a8, b6a4d5a, b7a9e69, b7b4e86, bcb1509, bfc58f5, c050ae4, c540976, c7af042, c97522f, ca8bd83, cd53924, d1f0e5f, d2d0fda, d48e330, db3d488, debe3d2, dfb236b, e0f3aae, e3181cf, e87d159, e9f8a11, ed0a8b8, f0d0d95, f176514, f281497, f617e86, f8725e8, f9c1850, fa46894)
- [GT-ZSTD-v1.5.7-0003] api: `ZSTD_getFrameHeader()` works on skippable frames (#4228) (PRs: #4136, #4217, #4226, #4227, #4228; commits: 0442e43, 04a2a02, 08edecb, 25bef24, 30671d7, 41c667c, 477a010, 5df80ac, 7bad787, 894ea31, 8d4506b, 9671813, a224572, a2ff6ea, f5d9d57, f8a2b35, fa46894)
- [GT-ZSTD-v1.5.7-0004] perf: substantial compression speed improvements (up to +30%) on small data, by @TocarIP (#4144) and @cyan4973 (#4165) (PRs: #4144, #4165; commits: 186b132, 197c258, 1e7fa24, 2cc600b, 741b860, 83de003, 8c38bda, 8e5823b, d45aee4, e8fce38, fa1fcb0)
- [GT-ZSTD-v1.5.7-0009] perf: slight compression ratio improvement thanks to better block boundaries (#4136, #4176, #4178) (PRs: #4038, #4136, #4167, #4176, #4178, #4180, #4191, #4210, #4217, #4220, #4228; commits: 01474bf, 0442e43, 04a2a02, 06b7cfa, 08edecb, 0be334d, 0d4b520, 1024aa9, 16450d0, 18b1e67, 1c62e71, 1ec5f9f, 20c3d17, 226ae73, 2366a87, 25bef24, 2dddf09, 30671d7, 31d48e9, 326c45b, 37706a6, 41c667c, 433f459, 4662f6e, 4685eaf, 477a010, 4ce91cb, 566763f, 57239c4, 586ca96, 5ae34e4, 5b4ce64, 5bae43b, 5df80ac, 6021b66, 6939235, 6dc5212, 6f2e29a, 73a6653, 7bad787, 7d3e5e3, 7f015c2, 7fb5347, 80a912d, 83a3402, 894ea31, 8b3887f, 8d4506b, 90095f0, 94d7b07, 9671813, 9e52789, a167571, a224572, a5bce4a, b68ddce, bbaba45, c80645a, ca6e55c, cae8d13, cdddcaa, d06e877, d0fe334, da2c0df, dd38c67, e190e79, e2d7d08, e557abc, e674035, ea85dc7, f83ed08, fa147cb, fa46894)
- [GT-ZSTD-v1.5.7-0019] portability: linux kernel branch, with improved support for Sequence producers (@embg, @gcabiddu, @cyan4973) (PRs: #4136; commits: e2d7d08, fa147cb)
- [GT-ZSTD-v1.5.7-0023] doc: clarify specification, by @elasota (PRs: #4226, #4227, #4228; commits: a2ff6ea, f8a2b35)
- [GT-ZSTD-v1.5.7-0027] Promoted ZSTD_getErrorCode() to a stable API, and updated the version number and related documentation comments. (Architecture-related: public API) (PRs: #4183, #4184; commits: d9553fd)
- [GT-ZSTD-v1.5.7-0029] Generalize the parameter and return value types of bit container operation functions from size_t to BitContainerType, so that the register type and size can be controlled independently of size_t. (Architecture-related: public API) (PRs: #4253; commits: 82346b9)
- [GT-ZSTD-v1.5.7-0034] Fixed the compilation warning of the zstd.h header file in the C++ environment, and added conditional compilation protection to be compatible with the -Wzero-as-null-pointer-constant option. (Architecture-related: public API) (PRs: #4034; commits: 97291fc, d7cb470)
- [GT-ZSTD-v1.5.7-0035] During the FSE decompression process, an error is thrown when the initial state of the Huffman weight is truncated. (Architecture-related: external behavior) (PRs: #4079; commits: 0938308)
- [GT-ZSTD-v1.5.7-0036] Fixed a memory leak caused by parameter checking when ZSTD_generateSequences returns early, moving the target buffer allocation after parameter checking. (Architecture-related: public API) (PRs: #4112, #4115; commits: a40bad8)
- [GT-ZSTD-v1.5.7-0039] Removed differences in row matcher selection based on SSE2/Neon availability, and unified the use of the same window log threshold to enhance reproducibility. (Architecture-related: platform compatibility) (PRs: #4230; commits: d88651e)
- [GT-ZSTD-v1.5.7-0040] Fixed the problem of error checking macro when building MSVC 64-bit, and adjusted the return type of two bit operation functions to BitContainerType. (Architecture-related: platform compatibility) (PRs: #4234; commits: 42d704a)
- [GT-ZSTD-v1.5.7-0041] Added CI tests for x86 32-bit + AVX2 combination, and fixed type conversion in BIT_closeCStream function. (Architecture-related: public API) (PRs: #4248, #4250; commits: 0501095, 35edbc2, 9efb097, d2d7461, f0b5f65)
- [GT-ZSTD-v1.5.7-0042] Fixed the compatibility issue of BMI2 built-in function on 32-bit platform, including selecting the correct built-in function according to size_t size, parameter type adjustment, conditional compilation format correction and enabling DYNAMIC_BMI2 support by default. (Architecture-related: platform compatibility) (PRs: #4248, #4252, #4265; commits: 0cda010, 26e5fb3, 462484d, 4bbf4a2, 936927a, ee17f4c)
- [GT-ZSTD-v1.5.7-0058] Rename the block splitter control parameter enumeration constant ZSTD_c_blockSplitter_level to ZSTD_c_blockSplitterLevel, and update related code and tests simultaneously. (Architecture-related: public API) (PRs: #4180; commits: 4f93206)
- [GT-ZSTD-v1.5.7-0062] The document clearly states that ZSTD_decompress() supports decompression of multiple consecutive compressed frames at one time, and the result will be splicing of all decompressed data. (Architecture-related: public API) (PRs: #4298; commits: 2acf904)

### Cross-cutting / Other Architecture-related Changes

- [GT-ZSTD-v1.5.7-0001] fix: compression bug in 32-bit mode associated with long-lasting sessions (PRs: #4129, #4136, #4290; commits: 09cb37c, 31d48e9, 468e145)
- [GT-ZSTD-v1.5.7-0005] perf: improved compression speed (~+5%) for dictionary compression at low levels (#4170) (PRs: #4170; commits: 18a4219, 730d2dc, c2abfc5, e63896e)
- [GT-ZSTD-v1.5.7-0008] perf: better speed for binaries on Windows (@pps83) and when compiled with Visual Studio (@MessyHack) (PRs: #4286, #4287; commits: 5883ee6, 6e1d02f, e117d79)
- [GT-ZSTD-v1.5.7-0011] perf: runtime bmi2 detection enabled on x86 32-bit mode (#4251) (PRs: #4248, #4251; commits: 9fbed33, a556559)
- [GT-ZSTD-v1.5.7-0013] cli: new `--max` command (#4290) (PRs: #4290; commits: 39d1d82, 468e145, 630b47a, 8ae1330, e3a9351, f86024c)
- [GT-ZSTD-v1.5.7-0014] build: improve `msbuild` version autodetection, support VS2022, by @ManuelBlanc (PRs: #4259; commits: 45c0e72, 897cec3, becef67)
- [GT-ZSTD-v1.5.7-0015] build: fix `meson` build by @artem and @Victor-C-Zhang, and on Windows by @bgilbert (PRs: #3931, #4087; commits: 1f72f52, 5be2a87)
- [GT-ZSTD-v1.5.7-0016] build: compatibility with Apple Framework, by @Treata11 (PRs: #4259; commits: 45c0e72, 897cec3, becef67)
- [GT-ZSTD-v1.5.7-0017] build: improve icc/icx compatibility, by @josepho0918 and @luau-project (PRs: #4046; commits: 2955d92)
- [GT-ZSTD-v1.5.7-0018] build: improve compatibility with Android NDK, by Adenilson Cavalcanti (PRs: #4103, #4107, #4299; commits: 5c465fc, c3c28c4)
- [GT-ZSTD-v1.5.7-0020] portability: improved qnx compatibility, suggested by @rainbowball (PRs: #4171, #4184, #4186, #4188; commits: 2e02cd3, 47d4f56, b3035b3)
- [GT-ZSTD-v1.5.7-0021] portability: improved install script for FreeBSD, by @sunpoet
- [GT-ZSTD-v1.5.7-0022] portability: fixed test suite compatibility with gnu hurd, by @diegonc (PRs: #4056, #4061, #4222; commits: f0937b8)

### Dictionary Builder Module

- [GT-ZSTD-v1.5.7-0057] The COVER algorithm dictionary training function is changed to be fully reentrant, using platform-related qsort_r/qsort_s instead of global variables to pass context, and providing a C90-compatible stable sort fallback implementation for BSD systems. (Architecture-related: platform compatibility) (PRs: #4045, #4086; commits: 345bcb5)

### Linux Kernel Integration Module

- [GT-ZSTD-v1.5.7-0025] Exposed external sequence producer API for Linux kernel modules, and added helper functions for calculating compression context workspace size. (Architectural Event: Linux Kernel Module) (PRs: #4063, #4064; commits: 3242ac5, be6a182)
- [GT-ZSTD-v1.5.7-0030] The ZSTD_compressSequencesAndLiterals() and ZSTD_CCtx_setParameter() functions are exposed in the kernel, and the build process and header file references are updated. (Architecture-related: public API) (PRs: #4260; commits: 92be4be)

### Seekable Format Module

- [GT-ZSTD-v1.5.7-0038] Add null pointer check before creating seek table to avoid segfault. (Architecture-related: public API) (PRs: #4201; commits: b683c0d)

## Routine Changes

### Bug Fixes

- [GT-ZSTD-v1.5.7-0043] Fixed ISO C incompatibility issue, replacing the empty initialization list of the structure with member-by-member assignment. (PRs: #4025; commits: 01cea2e, 4f41631)
- [GT-ZSTD-v1.5.7-0044] Decompression error messages now always show the full original filename, no longer truncated. (PRs: #4011; commits: a2f145f)
- [GT-ZSTD-v1.5.7-0045] Fixed zlibWrapper build error, changed type conversion in gz_write function from z_uInt to uInt. (PRs: #4021; commits: 71def59)
- [GT-ZSTD-v1.5.7-0046] Fixed multiple memory leaks and initialized variables to avoid undefined behavior. (PRs: #4025; commits: 1d5e970)
- [GT-ZSTD-v1.5.7-0047] Fixed the null pointer dereference problem in legacy/zstd_v06 caused by the lack of check for ZSTDv06_createDCtx allocation failure, and added memory release and null pointer return processing on failure. (PRs: #4026, #4050; commits: 1872688)
- [GT-ZSTD-v1.5.7-0048] Fixed an issue where pzstd could cause threads to hang due to the work queue not ending properly when decompressing corrupted files. (PRs: #4080; commits: 80af41e)
- [GT-ZSTD-v1.5.7-0049] Fixed the formatString_u function to correctly display numbers greater than 100, so that the benchmark can handle more than 100 files without the -S option. (PRs: #4110, #4113; commits: 89451ca)
- [GT-ZSTD-v1.5.7-0050] Fixed the issue of files not being closed in the BMK_loadFiles function. (PRs: #4151, #4158; commits: 8edd147)
- [GT-ZSTD-v1.5.7-0051] Fixed the problem of the benchmark module repeatedly displaying the loading summary in --quiet mode. Now the source file is only loaded once, and all compression levels are tested uniformly. (PRs: #4174; commits: 0079d51)
- [GT-ZSTD-v1.5.7-0052] Fixed type conversion warning in DEBUGLOG, changed format specifier from %lli to %i and explicitly converted parameter types. (PRs: #4180; commits: fcbf6b0)
- [GT-ZSTD-v1.5.7-0053] Fixed the problem of printing display error when the file size exceeds 4GB. (PRs: #4199; commits: 194062a)
- [GT-ZSTD-v1.5.7-0054] Fixed a bug where the optimal parser might generate matches that were too short when long distance matching was enabled, and changed the match length check from the hardcoded MINMATCH to the dynamic minMatch parameter. (PRs: #4223; commits: 1548bfc)
- [GT-ZSTD-v1.5.7-0055] Fixed the array index out-of-bounds access problem and added bounds check before access. (PRs: #4238; commits: e490be8)
- [GT-ZSTD-v1.5.7-0056] Fixed an array out-of-bounds access issue that may occur when the block delimiter is not found, and added corresponding error returns. (PRs: #4238; commits: afff3d2)
- [GT-ZSTD-v1.5.7-0081] fixed VS2010 solution (commits: 76ad1d6)

### Build and CI

- [GT-ZSTD-v1.5.7-0072] Fixed failure due to missing liblzma dependency in Meson and CMake Linux build tests, explicitly installing the liblzma-dev package in CI. (PRs: #4243; commits: 0e819c9, 196e76e, 80ff61d)
- [GT-ZSTD-v1.5.7-0073] On FreeBSD, use the system's own md5sum instead of gmd5sum. (PRs: #3994; commits: 103a85e)
- [GT-ZSTD-v1.5.7-0074] Fixed missing include directories for the resource compiler in CMake builds, setting the correct include path for rc. (PRs: #4019; commits: fd5f810)
- [GT-ZSTD-v1.5.7-0075] Updated the FreeBSD man page installation directory. (PRs: #4231; commits: 0fd5210)
- [GT-ZSTD-v1.5.7-0077] updated FreeBSD VM to 14.2 (commits: b73e06b)
- [GT-ZSTD-v1.5.7-0078] add prerelease option (commits: 7d63a1c)
- [GT-ZSTD-v1.5.7-0079] removed fullbench-dll project from visual solutions (commits: 47edd0a)
- [GT-ZSTD-v1.5.7-0080] update Visual Studio solutions (commits: 6f8c104)
- [GT-ZSTD-v1.5.7-0082] Update FreeBSD VM image to 14.1 (commits: a3b5c45)
- [GT-ZSTD-v1.5.7-0083] Drop FreeBSD 13.2 CI (commits: 949689f)
- [GT-ZSTD-v1.5.7-0084] Improve MSBuild search; add latest option (commits: 9c442d6)
- [GT-ZSTD-v1.5.7-0085] Use vswhere to find MSBuild; add VS2022 support (commits: 65ab6c2)

### Functional Changes / Refactorings

- [GT-ZSTD-v1.5.7-0060] Change the preprocessor condition from DYNAMIC_BMI2 != 0 to DYNAMIC_BMI2, migrate the STATIC_BMI2 macro definition to portability_macros.h, and uniformly use the STATIC_BMI2 macro check instead of ==1 comparison. (PRs: #4263, #4264, #4265; commits: 1204626, 1b15e88, f7e8fc3)
- [GT-ZSTD-v1.5.7-0061] Adjust the order of conditional judgment defined by the STATIC_BMI2 macro, giving priority to checking the __BMI2__ macro, and then using MSVC and __AVX2__ as alternatives. (PRs: #4264; commits: 0a18362)

### New Features

- [GT-ZSTD-v1.5.7-0012] cli: multi-threading as default CLI setting, by @daniellerozenblit (PRs: #4211; commits: 17beeb5)
- [GT-ZSTD-v1.5.7-0031] In benchmark mode, when combined with the -v option, the number of threads used is now displayed, and the display information of the benchmark is optimized. (PRs: #4235; commits: 5650004)
- [GT-ZSTD-v1.5.7-0032] When using the --long or --patch-from option, --ultra is now automatically enabled without the user having to specify it explicitly. (PRs: #4289; commits: aebffd6)

### Performance

- [GT-ZSTD-v1.5.7-0006] perf: much faster speed for `--patch-from` at high compression levels (#4276) (PRs: #4276, #4288; commits: 220abe6, 23e5f80, 34ba144, 4609a40, 7406d2b, 85a44b2, c7cd7dc, e637fc6, ef2bf57, f11bd19, ffa66a6)
- [GT-ZSTD-v1.5.7-0007] perf: higher `--patch-from` compression ratios, notably at high levels (#4288) (PRs: #4094, #4139, #4146, #4276, #4288; commits: 039f404, 09d7e34, 220abe6, 339bca6, 34ba144, 4609a40, 67fad95, 72406b7, 7406d2b, b320d09, bf218c1, d2c562b, d5e4698, d84d70b, f26cc54, ffa66a6)
- [GT-ZSTD-v1.5.7-0010] perf: slight compression ratio improvement for `dfast`, aka levels 3 and 4 (#4171) (PRs: #4160, #4171, #4180; commits: 41d870f, 47d4f56, 61d08b0, 6326775, b84653f, b880f20, f593ccd, ff8e98b)

### Tests

- [GT-ZSTD-v1.5.7-0024] misc: improved tests/decodecorpus validation tool (#4102), by antmicro (PRs: #4102; commits: 1f5df58, fdfb2af)
