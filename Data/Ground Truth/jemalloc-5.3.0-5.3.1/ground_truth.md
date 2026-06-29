# Ground Truth for jemalloc-5.3.0-5.3.1

## Important Changes

### Architecture-related Changes

- [GT-JEMALLOC-5.3.1-0084] Added infrastructure for the tcache batching function, including introducing the bin type with batch processing capabilities, initializing batcher, handling fork locks, and adding new batch allocation functions to improve multi-threading performance. (Architecture-related: public API) (PRs: #2608, #2695, #2710; commits: 60f472f, 8c54637, c085530, f9c0b5f, fc61573)
- [GT-JEMALLOC-5.3.1-0086] The platform abstraction layer has been enhanced, reentrant safe malloc_open and malloc_close helper functions have been added and system calls have been replaced, and a frame pointer-based safe traceback unwinder has been added to support mixed compilation environments. (Architecture-related: platform compatibility) (PRs: #2706, #2712; commits: 8c2e15d, edc1576)

### Arena & Metadata Layer

- [GT-JEMALLOC-5.3.1-0063] Redesign tcache GC to regulate the frequency and make it locality-aware. The new design is default on, guarded by option `experimental_tcache_gc`. (@nullptr0-0: 0c88be9e, e2c9f3a9, 14d5dc13, @deadalnix: 5afff2e4) (PRs: #2643, #2685; commits: 0c88be9, 14d5dc1, 5afff2e, e2c9f3a, f68effe)
- [GT-JEMALLOC-5.3.1-0073] Move the bin-related functions in arena.c to bin.c, add the bin_ prefix uniformly, and change the functions that rely on arena_is_auto check to accept the is_auto parameter. (Architecture event: core internal module reorganization) (PRs: #2864; commits: 1cc563f)
- [GT-JEMALLOC-5.3.1-0096] Fixed the arena selection incorrectly using the global oversize_threshold when over-large allocation, instead using each arena's own threshold. (Architecture-related: public API) (PRs: #2460; commits: 86eb49b)
- [GT-JEMALLOC-5.3.1-0149] Mark arena's bins field as deprecated, change internal code to access it through the all_bins field, and suppress warnings for known legal locations. (Architecture-related: public API) (PRs: #2506; commits: 424dd61)

### Cross-cutting / Other Architecture-related Changes

- [GT-JEMALLOC-5.3.1-0005] Add compile-time option `--enable-force-getenv` to use `getenv` instead of `secure_getenv`. (@interwq: 481bbfc9) (PRs: #2352; commits: 481bbfc)
- [GT-JEMALLOC-5.3.1-0006] Add compile-time option `--disable-dss` to disable the usage of `sbrk(2)`. (@Svetlitski: ea5b7bea) (PRs: #2476; commits: ea5b7be)
- [GT-JEMALLOC-5.3.1-0009] Add compile-time option `--disable-user-config` to disable reading the runtime configurations from `/etc/malloc.conf` or environment variable `MALLOC_CONF`. (@roblabla: c17bf8b3) (PRs: #2690; commits: c17bf8b)
- [GT-JEMALLOC-5.3.1-0012] Add mallctl interfaces: (PRs: #1421, #2730, #2869, #2882; commits: 6515df8, 8c2b8bc, b8646f4)
- [GT-JEMALLOC-5.3.1-0022] Make mallctl `arenas.lookup` triable without crashing on invalid pointers. (@auxten: 019cccc2, 5bac3849) (PRs: #2424; commits: 019cccc, 5bac384)
- [GT-JEMALLOC-5.3.1-0025] Fix the pkg-config metadata file. (@BtbN: ed7e6fe7, ce8ce99a) (PRs: #2525, #2526; commits: ce8ce99, ed7e6fe)
- [GT-JEMALLOC-5.3.1-0042] Fix incorrect printing on 32bit. (@sundb: 630434bb) (PRs: #2600; commits: 630434b)
- [GT-JEMALLOC-5.3.1-0047] Remove `unreachable()` macro conditionally to prevent definition conflicts for C23+. (@appujee: d8486b26, 4b88bddb) (PRs: #2748; commits: 4b88bdd, d8486b2)
- [GT-JEMALLOC-5.3.1-0049] Change the default page size to 64KB on aarch64 Linux. (@lexprfuncall: 9442300c) (PRs: #2864; commits: 9442300)
- [GT-JEMALLOC-5.3.1-0050] Update config.guess and config.sub to the latest version. (@lexprfuncall: c51949ea) (PRs: #1421, #2465, #2508, #2730, #2814, #2869, #2882; commits: 162ff83, 46e464a, 6515df8, 8c2b8bc, b8646f4, c51949e)
- [GT-JEMALLOC-5.3.1-0051] Determine the page size on Android from NDK header files. (@lexprfuncall: c51abba1) (PRs: #2657, #2864; commits: c51abba)
- [GT-JEMALLOC-5.3.1-0052] Improve the portability of grep patterns in configure.ac. (@lexprfuncall: 365747bc) (PRs: #2396, #2750, #2777, #2864; commits: 365747b, 6743518, a361e88, d503d72)
- [GT-JEMALLOC-5.3.1-0053] Add compile-time option `--with-cxx-stdlib` to specify the C++ standard library. (@yuxuanchen1997: a10ef3e1) (PRs: #2864; commits: a10ef3e)
- [GT-JEMALLOC-5.3.1-0059] Allocate thread cache using the base allocator, which enables thread cache to use thp when `metadata_thp` is turned on. (@interwq: 72cfdce7) (PRs: #2537; commits: 72cfdce)
- [GT-JEMALLOC-5.3.1-0069] Update profiling internals with an example. (@jordalgo: b04e7666) (PRs: #2339; commits: b04e766)

### Extent & Page Management Layer

- [GT-JEMALLOC-5.3.1-0003] Add compile-time option `--enable-pageid` to enable memory mapping annotation. (@devnexen: 4fc5c4fb) (commits: 4fc5c4f)
- [GT-JEMALLOC-5.3.1-0011] Enable process_madvise usage, add runtime option `process_madvise_max_batch` to control the max # of regions in each madvise batch. (@interwq: 22440a02, @spredolac: 4246475b) (PRs: #2794, #2841, #2864; commits: 22440a0, 4246475, 852da1b)
- [GT-JEMALLOC-5.3.1-0044] Fix mmap tag conflicts on MacOS. (@kdrag0n: c893fcd1) (PRs: #2659; commits: c893fcd)
- [GT-JEMALLOC-5.3.1-0046] Fix VM over-reservation on systems with larger pages, e.g., aarch64. (@interwq: cd05b19f) (PRs: #2628; commits: 3383b98, cd05b19)
- [GT-JEMALLOC-5.3.1-0072] Extract the hpa_central component from the hpa source file and migrate it to the new file src/hpa_central.c. (Architecture event: Core internal module reorganization) (PRs: #2864; commits: 8a06b08)
- [GT-JEMALLOC-5.3.1-0076] Transfer the ownership of the SEC cache to the HPA shard, simplify the code implementation, add fine-grained statistical information for each bin, and introduce a per-bin granular locking mechanism. (Architecture-related: Module responsibility changes) (PRs: #2864, #2873; commits: 6016d86, 6281482)
- [GT-JEMALLOC-5.3.1-0083] HPA allows frequently reused allocations to bypass the slab_max_alloc limit and adds a new batch allocation function. (Architecture-related: public API) (PRs: #2593; commits: a2c5267)
- [GT-JEMALLOC-5.3.1-0088] The HPA largepage allocator adds sliding window-based peak demand tracking, huge page initialization capabilities, time-based cleanup delay and smart candidate selection, and an experimental option to force hugify. (Architecture-related: public API) (PRs: #2780, #2864; commits: 47aeff1, a199278, ad108d5)
- [GT-JEMALLOC-5.3.1-0097] Fix an issue with HPA configuration that could cause an infinite purge loop, verifying HPA settings at the end of configuration parsing and normalizing or aborting based on the abort_conf option. (Architecture-related: configuration behavior) (PRs: #2449, #2484; commits: 3aae792)
- [GT-JEMALLOC-5.3.1-0103] Disable the psset test under an excessively large hugepage, and add false logic to return false when the hugepage size exceeds the limit in the HPA support check. (Architecture-related: platform compatibility) (PRs: #2770; commits: 587676f)
- [GT-JEMALLOC-5.3.1-0152] Reconstruct the HPA cleaning logic, add a vectorized cleaning function for batch processing of multiple large pages, and extract independent tool functions to support cross-page calls. (Architecture-related: public API) (PRs: #2827; commits: cfa90df)
- [GT-JEMALLOC-5.3.1-0153] Removed the pidfd_open system call, used the PIDFD_SELF constant instead, and added errno save/restore and process madvise gate checks. (Architecture-related: platform compatibility) (PRs: #2864; commits: 5d5f76e)
- [GT-JEMALLOC-5.3.1-0155] Reconstruct the Transparent Huge Page (THP) state initialization logic, extract the function that determines whether to skip setting the THP state, and output init_system_thp_mode in malloc statistics. (Architecture-related: public API) (PRs: #2864; commits: 2cfa419)
- [GT-JEMALLOC-5.3.1-0160] Introduce the option experimental_hpa_max_purge_nhp, which limits the maximum number of hugepages cleaned in each cleaning operation and provides backward-compatible behavior control. (Architecture-related: public API) (PRs: #2686; commits: aaa2900)
- [GT-JEMALLOC-5.3.1-0161] Support HPA vectorized cleanup, use process_madvise to reduce system calls, support vectorized cleanup across multiple large pages, and introduce a batch processing mechanism to limit the number of ranges for each system call. (Architecture-related: public API) (PRs: #2820, #2827; commits: 1956a54, f19f49e)

### Instrumentation & Profiling Layer

- [GT-JEMALLOC-5.3.1-0004] Add runtime option `prof_bt_max` to control the max stack depth for profiling. (@guangli-dai: a0734fd6) (PRs: #2319; commits: a0734fd)
- [GT-JEMALLOC-5.3.1-0013] `opt.prof_bt_max` (@guangli-dai: a0734fd6) (PRs: #2319; commits: a0734fd)
- [GT-JEMALLOC-5.3.1-0014] `arena.<i>.name` to set and get arena names. (@guangli-dai: ba19d2cb) (PRs: #2325, #2381; commits: b612512, ba19d2c)
- [GT-JEMALLOC-5.3.1-0024] Fix jemalloc's `read(2)` and `write(2)`. (@Svetlitski: d2c9ed3d, @lexprfuncall: 9fdc1160) (PRs: #2516, #2864; commits: 9fdc116, d2c9ed3)
- [GT-JEMALLOC-5.3.1-0034] Fix large alloc nrequests under-counting on cache misses. (@spredolac: 3cc56d32) (PRs: #2873; commits: 3cc56d3)
- [GT-JEMALLOC-5.3.1-0035] Fix the build in C99. (@abaelhe: 56ddbea2) (PRs: #2322; commits: 56ddbea)
- [GT-JEMALLOC-5.3.1-0036] Add `pthread_setaffinity_np` detection for non Linux/BSD platforms. (@devnexen: 4c95c953) (PRs: #2341; commits: 4c95c95)
- [GT-JEMALLOC-5.3.1-0037] Make `VARIABLE_ARRAY` compatible with compilers not supporting VLA, i.e., Visual Studio C compiler in C11 or C17 modes. (@madscientist: be65438f) (PRs: #2347; commits: be65438)
- [GT-JEMALLOC-5.3.1-0039] Reduce the memory overhead in small allocation sampling for systems with larger page sizes, e.g., ARM. (@Svetlitski: 5a858c64) (PRs: #2358, #2459; commits: 5a858c6)
- [GT-JEMALLOC-5.3.1-0041] Enable heap profiling on MacOS. (@nullptr0-0: 4b555c11) (PRs: #2610; commits: 4b555c1)
- [GT-JEMALLOC-5.3.1-0045] Fix monotonic timer assumption for win32. (@burtonli: 8dc97b11) (PRs: #2669; commits: 8dc97b1)
- [GT-JEMALLOC-5.3.1-0048] Fix dlsym failure observed on FreeBSD. (@rhelmot: 86bbabac) (PRs: #2812; commits: 86bbaba)
- [GT-JEMALLOC-5.3.1-0057] Inline the storage for thread name in the profiling data. (@interwq: ce0b7ab6, e62aa478) (PRs: #2407; commits: 6cab460, ce0b7ab, e62aa47)
- [GT-JEMALLOC-5.3.1-0066] Refactor thread events to allow registration of users' thread events and remove prof_threshold as the built-in event. (@spredolac: e6864c60, 015b0179, 34ace916) (PRs: #2864; commits: 015b017, 34ace91, e6864c6)
- [GT-JEMALLOC-5.3.1-0071] Split the TSD implementation details into a new tsd_internals.h file, so that each TSD implementation header file explicitly includes its dependencies, and the header file is self-contained. (Architecture event: core internal module reorganization) (PRs: #2463; commits: 856db56)
- [GT-JEMALLOC-5.3.1-0074] Separate the code related to configuration parsing and initialization from src/jemalloc.c and separate it into the src/conf.c file. (Architecture event: core internal module reorganization) (PRs: #2864; commits: ad726ad)
- [GT-JEMALLOC-5.3.1-0077] Added experimental USDT SystemTap probe support, and added multiple tracking points in HPA, sec and other modules. (Architecture event: USDT probe support) (PRs: #2864; commits: 711fff7, d70882a, f87bbab)
- [GT-JEMALLOC-5.3.1-0079] Added experimental prof_sample and prof_sample_free hooks, allowing advanced users to track additional information when allocating and freeing sample objects. (Architecture-related: public API) (PRs: #2360; commits: 8580c65)
- [GT-JEMALLOC-5.3.1-0082] Added pid namespace support to the heap profile file name. When this option is enabled, the file name will contain a namespace identifier to distinguish processes in different namespaces. (Architecture-related: public API) (PRs: #2636; commits: 11038ff)
- [GT-JEMALLOC-5.3.1-0085] The public API for page allocator shard statistics has been expanded, three new getter functions pa_shard_nactive, pa_shard_ndirty and pa_shard_nmuzzy have been added, and psset internal status statistics are exposed to mallctl and malloc statistics output. (Architecture-related: public API) (PRs: #2622, #2761; commits: 6092c98, b2e59a9)
- [GT-JEMALLOC-5.3.1-0087] Optimized time-related functions, added support for clock_gettime_nsec_np to replace mach_absolute_time, and added a new nstime_ms_since function, which is also abbreviated to nstime_ms. (Architecture-related: public API) (PRs: #2733, #2746; commits: 6d625d5, b9758af)
- [GT-JEMALLOC-5.3.1-0093] Fix the macro definition of PowerPC architecture in quantum.h, expand the detection conditions to support more PowerPC variants, and ensure correct compilation on platforms such as Darwin PPC. (Architecture-related: platform compatibility) (PRs: #2281; commits: 70e3735)
- [GT-JEMALLOC-5.3.1-0094] Fix build issues for the OpenBSD platform, enable pthread name-related APIs, and disable per-thread CPU affinity handling not supported by that platform. (Architecture-related: Platform Compatibility) (commits: 5847841)
- [GT-JEMALLOC-5.3.1-0095] Fix the segmentation fault caused by empty nodes in the red-black tree deletion operation, adjust the parameter type of the large memory release safety check function and increase the size upper limit check. (Architecture-related: public API) (PRs: #2433; commits: 90176f8)
- [GT-JEMALLOC-5.3.1-0101] Fixed the problem that oversize_arena cannot create background threads when background_thread is enabled, ensuring that the cleanup operation does not stall under low arena numbers. (Architecture-related: public API) (PRs: #2466, #2642; commits: 8d8379d)
- [GT-JEMALLOC-5.3.1-0102] Add configure to check whether the gettid() function exists, and add conditional compilation in prof_stack_range.c, and fix macro definition errors to ensure compatibility on old glibc versions. (Architecture-related: platform compatibility) (PRs: #2754, #2786; commits: 17881eb, 20cc983)
- [GT-JEMALLOC-5.3.1-0148] Optimize the lock acquisition logic, no longer set the locked flag when acquisition fails, avoid unnecessary spin, and improve concurrency performance. (Architecture-related: external behavior) (PRs: #2371; commits: 5f64ad6)
- [GT-JEMALLOC-5.3.1-0156] Rollback changes to the experimental configuration option "prefetch from cache_bin fast path". (Architecture-related: configuration interface) (PRs: #2864; commits: d4908fe)

### Thread-Local Caching Layer

- [GT-JEMALLOC-5.3.1-0061] Optimize thread-local storage implementation on Windows. (@mcfi: 9e123a83, 3a0d9cda) (PRs: #2583, #2702; commits: 3a0d9cd, 9e123a8)
- [GT-JEMALLOC-5.3.1-0154] Replace direct comparison of thread IDs with calls to pthread_equal to improve portability and reliability. (Architecture-related: Platform compatibility) (PRs: #2864; commits: 5a634a8)

### public API Layer

- [GT-JEMALLOC-5.3.1-0001] Support pvalloc. (@Lapenkov: 5b1f2cc5) (PRs: #2257; commits: 5b1f2cc)
- [GT-JEMALLOC-5.3.1-0002] Add double free detection for the debug build. (@izaitsevfb: 36366f3c, @guangli-dai: 42daa1ac, @divanorama: 1897f185) (PRs: #2315; commits: 1897f18, 36366f3, 42daa1a)
- [GT-JEMALLOC-5.3.1-0007] Add runtime option `tcache_ncached_max` to control the number of items in each size bin in the thread cache. (@guangli-dai: 8a22d10b) (PRs: #2530, #2555; commits: 630f7de, 8a22d10)
- [GT-JEMALLOC-5.3.1-0008] Add runtime option `calloc_madvise_threshold` to determine if kernel or memset is used to zero the allocations for calloc. (@nullptr0-0: 5081c16b) (PRs: #2631; commits: 5081c16)
- [GT-JEMALLOC-5.3.1-0010] Add runtime option `disable_large_size_classes` to guard the new usable size calculation, which minimizes the memory overhead for large allocations, i.e., >= 4 * PAGE. (@guangli-dai: c067a55c, 8347f104) (PRs: #2646, #2835; commits: 8347f10, c067a55)
- [GT-JEMALLOC-5.3.1-0015] `thread.tcache.max` to set and get the `tcache_max` of the current thread. (@guangli-dai: a442d9b8) (PRs: #2493; commits: a442d9b)
- [GT-JEMALLOC-5.3.1-0016] `thread.tcache.ncached_max.write` and `thread.tcache.ncached_max.read_sizeclass` to set and get the `ncached_max` setup of the current thread. (@guangli-dai: 630f7de9, 6b197fdd) (PRs: #2530, #2555; commits: 630f7de, 6b197fd, 6fb3b6a, 8a22d10)
- [GT-JEMALLOC-5.3.1-0017] `arenas.hugepage` to return the hugepage size used, also exported to malloc stats. (@ilvokhin: 90c627ed) (PRs: #2652; commits: 90c627e)
- [GT-JEMALLOC-5.3.1-0018] `approximate_stats.active` to return an estimate of the current active bytes, which should not be compared with other stats retrieved. (@guangli-dai: 0988583d) (PRs: #2864; commits: 0988583)
- [GT-JEMALLOC-5.3.1-0021] Add null pointer detections in mallctl calls. (@Svetlitski: dc0a184f, 0288126d) (PRs: #2431, #2436; commits: 0288126, dc0a184)
- [GT-JEMALLOC-5.3.1-0027] Fix `rallocx()` to set errno to ENOMEM upon OOMing. (@arter97: 38056fea, @interwq: 83b07578) (PRs: #2620, #2633; commits: 38056fe, 83b0757)
- [GT-JEMALLOC-5.3.1-0029] Fix background thread initialization race. (@puzpuzpuz: 4d0ffa07) (PRs: #2864; commits: 4d0ffa0)
- [GT-JEMALLOC-5.3.1-0031] Handle tcache init failures gracefully. (@lexprfuncall: a056c20d) (PRs: #2864; commits: a056c20)
- [GT-JEMALLOC-5.3.1-0038] Fix the build on Linux using musl library. (@marv: aba1645f, 45249cf5) (PRs: #2338; commits: 45249cf, aba1645)
- [GT-JEMALLOC-5.3.1-0040] Add C23's `free_sized` and `free_aligned_sized`. (@Svetlitski: cdb2c0e0) (PRs: #2482; commits: cdb2c0e)
- [GT-JEMALLOC-5.3.1-0043] Make `JEMALLOC_CXX_THROW` compatible with C++ versions newer than C++17. (@r-barnes, @guangli-dai: 21bcc0a8) (PRs: #2656; commits: 21bcc0a)
- [GT-JEMALLOC-5.3.1-0070] The experimental thread activity callback function has been removed, and the related code has been cleaned up. (Architecture-related: public API removed) (PRs: #2876; commits: 176ea0a)
- [GT-JEMALLOC-5.3.1-0075] Remove the build-time configuration config_limit_usize_gap, and simplify the conditional judgment in related functions. (Architecture-related: build configuration) (PRs: #2835; commits: 01e9ecb)
- [GT-JEMALLOC-5.3.1-0078] The malloc_getcpu function is implemented on the amd64 and arm64 architectures of macOS, and per-CPU area allocation is enabled. (Architecture-related: public API) (PRs: #2280, #2291; commits: 4e12d21, df8f7d1)
- [GT-JEMALLOC-5.3.1-0080] Added support for compile-time malloc_conf override in jemalloc_internal_overrides.h. (Architecture-related: compile-time configuration override) (PRs: #2453, #2499; commits: a2259f9, b01d496)
- [GT-JEMALLOC-5.3.1-0081] Added support for the deprecated attribute, and added diagnostic macros for suppressing deprecated declaration warnings. (Architecture-related: public API) (PRs: #2506; commits: 120abd7)
- [GT-JEMALLOC-5.3.1-0098] Remove the incorrectly introduced intermediate generated header files included in the public header file jemalloc.h (architecture-related: public API) (PRs: #2489, #2492; commits: 8ff7e7d)
- [GT-JEMALLOC-5.3.1-0099] Allow zero-sized memalign allocations to pass and no longer trigger assertion failures. (Architecture-related: public API) (PRs: #1554, #2606; commits: 1aba4f4)
- [GT-JEMALLOC-5.3.1-0100] Fix and remove the temporary option experimental_hpa_strict_min_purge_interval, so that the minimum purge interval check always takes effect, and fix the logical error that this option causes only one page to be purged at a time, and instead purge multiple pages at once after the minimum interval is met. (Architecture-related: public API) (PRs: #2686, #2701; commits: 143f458, 4f4fd42)
- [GT-JEMALLOC-5.3.1-0104] Fixed the problem of not checking the input to be 0 when setting max_background_threads via mallctl. Now the 0 value will be rejected and an error will be returned. (Architecture-related: external behavior) (PRs: #2787; commits: 607b866)
- [GT-JEMALLOC-5.3.1-0105] Move extern "C" declarations to only required locations, fix error in compiling C++ code when clang modules are enabled. (Architecture-related: public API) (PRs: #2821; commits: 80e9001)
- [GT-JEMALLOC-5.3.1-0106] Fixed the return value error caused by the lack of inversion operation when usize_min in the large_ralloc_no_move function was rolled back, and added corresponding unit tests. (Architecture-related: public API) (PRs: #2873; commits: a0f2bdf)
- [GT-JEMALLOC-5.3.1-0107] Fixed an issue where conf_handle_char_p could incorrectly modify the buffer when the target buffer size was zero, and removed the unused conf_handle_unsigned function. (Architecture-related: Configuration processing behavior) (PRs: #2873; commits: b507644)
- [GT-JEMALLOC-5.3.1-0150] Remove unnecessary parameters in the cache_bin_postincrement function call and adjust related code formats. (Architecture-related: public API) (PRs: #2493; commits: fbca96c)
- [GT-JEMALLOC-5.3.1-0151] Rename option hpa_strict_min_purge_interval to experimental_hpa_strict_min_purge_interval to clarify its experimental nature. (Architecture-related: public API) (PRs: #2686; commits: c7ccb8d)
- [GT-JEMALLOC-5.3.1-0171] Add explicit unsigned type conversion to MALLOCX_ARENA and MALLOCX_TCACHE macros. (Architecture-related: public API) (PRs: #2445; commits: d577e9b)

## Routine Changes

### Bug Fixes

- [GT-JEMALLOC-5.3.1-0019] Prevent potential deadlocks in decaying during reentrancy. (@interwq: 434a68e2) (PRs: #2409; commits: 434a68e)
- [GT-JEMALLOC-5.3.1-0020] Fix segfault in extent coalescing. (@Svetlitski: 12311fe6) (PRs: #2432; commits: 12311fe)
- [GT-JEMALLOC-5.3.1-0023] Demote sampled allocations for proper deallocations during `arena_reset`. (@Svetlitski: 62648c88) (PRs: #2496; commits: 62648c8)
- [GT-JEMALLOC-5.3.1-0026] Fix the autogen.sh so that it accepts quoted extra options. (@honggyukim: f6fe6abd) (commits: f6fe6ab)
- [GT-JEMALLOC-5.3.1-0028] Avoid stack overflow for internal variable array usage. (@nullptr0-0: 47c9bcd4, 48f66cf4, @xinydev: 9169e927) (PRs: #2677, #2846; commits: 47c9bcd, 48f66cf, 9169e92)
- [GT-JEMALLOC-5.3.1-0030] Guard os_page_id against a NULL address. (@lexprfuncall: 79cc7dcc) (PRs: #2864; commits: 79cc7dc)
- [GT-JEMALLOC-5.3.1-0032] Fix missing release of acquired neighbor edata in extent_try_coalesce_impl. (@spredolac: 675ab079) (PRs: #2873; commits: 675ab07)
- [GT-JEMALLOC-5.3.1-0033] Fix memory leak of old curr_reg on san_bump_grow_locked failure. (@spredolac: 5904a421) (PRs: #2873; commits: 5904a42)
- [GT-JEMALLOC-5.3.1-0108] Fix the error when compiling edata.h in MSVC 2019, and change the composite literal initialization in the edata_cmp_summary_get function to declare the variable first and then assign the value. (PRs: #2275; commits: 70d4102)
- [GT-JEMALLOC-5.3.1-0109] Fix the assertion failure problem in arena_stats_merge() caused by improper reading order of nmalloc and ndalloc, and avoid race conditions by exchanging the reading order. (PRs: #2234, #2304; commits: cb578bb)
- [GT-JEMALLOC-5.3.1-0110] Fixed a race condition issue when updating thread names in heap analysis to avoid temporary emptying, causing the analysis read path to obtain null values. (PRs: #2380; commits: 5fd5583)
- [GT-JEMALLOC-5.3.1-0111] Fix the assignment error in the assertion statement in hpa_from_pai, change the assignment operator to the equality operator, and ensure that the assertion correctly checks pointer equality. (PRs: #2412, #2415; commits: 521970f)
- [GT-JEMALLOC-5.3.1-0112] Removed a wrong assertion in arena_extent_alloc_large that could trigger falsely due to delayed work when HPA was enabled. (PRs: #2107, #2418; commits: fc68012)
- [GT-JEMALLOC-5.3.1-0113] Fix the thread name reference in prof_recent dump to ensure that the thread name pointer is passed correctly; and add the prof_sys_thread_name attribute in the prof_recent unit test to fix testing problems in environments without a default thread name. (PRs: #2407, #2434, #2435; commits: 94ace05, d4a2b8b)
- [GT-JEMALLOC-5.3.1-0114] Fix the bug that hpa_shard is not destroyed correctly, replace the incorrectly called hpa_shard_disable with hpa_shard_destroy. (PRs: #2448; commits: 9c32689)
- [GT-JEMALLOC-5.3.1-0115] Fixed the uninitialized data reading problem in prof_free caused by the security check path of arena_prof_info_get not initializing prof_info->alloc_tctx. (PRs: #2433, #2464; commits: 210f0d0)
- [GT-JEMALLOC-5.3.1-0116] Fix memory usage statistics for sampled small allocations, now correctly counting allocations for their effective bin size, rather than incorrectly attributed to large object classes; and add test cases to verify that sampled small memory allocations maintain expected page alignment and metadata invariants. (PRs: #2459, #2478, #2486; commits: 07a2eab, ebd7e99)
- [GT-JEMALLOC-5.3.1-0117] On configuration parsing errors, the error message now contains the fragment of the configuration string that caused the problem. (PRs: #2503; commits: 6816b23)
- [GT-JEMALLOC-5.3.1-0118] Fixed an error in the register used when reading the CPU ID via the rdtscp instruction, correcting the register from edx to ecx. (PRs: #2527, #2529; commits: b71da25)
- [GT-JEMALLOC-5.3.1-0119] Fixed the bug that promoted allocation may not be correctly recognized as promoted when released, and adjusted the conditional judgment logic in arena_dalloc_large. (PRs: #2530; commits: 867eedf)
- [GT-JEMALLOC-5.3.1-0120] Fix the bug that nfill may be 0 when ncached_max is 1, make sure it is set to 1 when nfill is 0, and add corresponding assertions. (PRs: #2555; commits: d88fa71)
- [GT-JEMALLOC-5.3.1-0121] Fix the infinite cleanup loop in HPA caused by hpa_hugify_blocked_by_ndirty still returning true when there is no dirty memory, and add regression tests; at the same time, simplify the delayed work processing logic. (PRs: #2533, #2632, #2686; commits: 0a9f51d, 47d69b4)
- [GT-JEMALLOC-5.3.1-0122] Fixed the sanity check of ncached and nstashed during tcache flush. When there are many stash items, ncached may be lower than the remaining value after flush stashed. In this case, flush can return directly. (PRs: #2637; commits: fa451de)
- [GT-JEMALLOC-5.3.1-0123] Fixed the problem that the locked flag in malloc_mutex_trylock was not set correctly, and added the lock status checking function malloc_mutex_is_locked() and assertion verification. (PRs: #2718; commits: 1960536, 661fb1e)
- [GT-JEMALLOC-5.3.1-0124] Fixed the problem that the locked status was not updated correctly when pthread_cond_wait internally released and reacquired the mutex lock. A new background_thread_cond_wait function was added to explicitly maintain this status. (PRs: #2718; commits: 3eb7a4b)
- [GT-JEMALLOC-5.3.1-0125] Mutex owner checks are skipped during background thread startup because some mutexes have not yet been initialized and the global initialization lock has overridden all locking operations. (PRs: #2719; commits: 44db479)
- [GT-JEMALLOC-5.3.1-0126] Fixed size calculation issue with error message in sized-dealloc safety check. (PRs: #2738; commits: 2a693b8)
- [GT-JEMALLOC-5.3.1-0127] Removed configuration validation for the HPA ratio (sum of hpa_dirty_mult and hpa_hugification_threshold) and removed the associated misconfiguration flagging logic. (PRs: #2762; commits: 3820e38)
- [GT-JEMALLOC-5.3.1-0128] Fixed the out-of-bounds read problem in the bitmap_ffu function caused by not checking the array boundary, and adjusted the loop logic to avoid loading data at invalid indexes. (PRs: #2789; commits: ef8e512)
- [GT-JEMALLOC-5.3.1-0129] Fixed the issue where the deferral_allowed flag was not set correctly when arena 0 was initialized, and added a test case to verify the fix. (PRs: #2795; commits: 499f306)
- [GT-JEMALLOC-5.3.1-0130] Fixed an issue with profiling sample metadata lookup in xallocx and added coverage of sdallocx paths in tests. (PRs: #2806; commits: ac279d7)
- [GT-JEMALLOC-5.3.1-0131] Fixed the frame pointer-based backtrace to handle stack range changes and fallback to the Linux backtrace function when a change is detected. (PRs: #2811; commits: 773b580)
- [GT-JEMALLOC-5.3.1-0132] Fixed the assertion error caused by repeated calls of huge_arena_auto_thp_switch when deleting and rebuilding b0 in the unit test, and ensured that automatic switching can take effect correctly after turning on huge arena before initialization. (PRs: #2818; commits: 3688dfb)
- [GT-JEMALLOC-5.3.1-0133] Added check for input size exceeding maximum class size in double-release validation. (PRs: #2854; commits: fd60645)
- [GT-JEMALLOC-5.3.1-0134] Fixed an issue where dehugify was incorrectly executed when purging, and related test cases were added and updated. (PRs: #2864; commits: a156e99)
- [GT-JEMALLOC-5.3.1-0135] Save and restore errno when calling process_madvise to avoid accidentally modifying the errno value due to system call failure. (PRs: #2864; commits: 5e98585)
- [GT-JEMALLOC-5.3.1-0136] Rolled back the "do not cancel huge pages when clearing" changes, restored the dehugify function and its calls, and added related tests and USDT tracking. (PRs: #2864; commits: 2688047)
- [GT-JEMALLOC-5.3.1-0137] Fixed an issue where locks were released prematurely before allocation after inserting a new page from central, ensuring mutex locks are maintained during allocation. (PRs: #2864; commits: 87555df)
- [GT-JEMALLOC-5.3.1-0138] Corrected the page initialization parameters when extracting from central, changed hugify_eager to start_as_huge, and added related test cases. (PRs: #2864; commits: 3678a57)
- [GT-JEMALLOC-5.3.1-0139] Fixed an issue where the derivation counter was not skipped correctly when outputting mutex lock statistics in malloc statistics in JSON format, resulting in an incorrect array index. (PRs: #2864; commits: 12b33ed)
- [GT-JEMALLOC-5.3.1-0140] Fixed an index underflow and assertion failure that could result from psset_pick_purge when rejecting time-incompatible candidate entries, and added corresponding unit tests. (PRs: #2871; commits: d758349)
- [GT-JEMALLOC-5.3.1-0141] Fixed the out-of-bounds check errors in arenas_bin_i_index and arenas_extent_i_index, changed the greater-than sign to the greater-than-equal sign, to prevent out-of-bounds reads from accessing indexes beyond the valid range; and added a unit test for boundary index returns ENOENT. (PRs: #2873; commits: 513778b)
- [GT-JEMALLOC-5.3.1-0142] Fixed the issue where the nactive_huge key was repeated and the ndirty_huge key was missing in the full_slabs and empty_slabs JSON segments in the HPA shard statistics output, and a unit test was added to verify that both segments contain ndirty_huge. (PRs: #2873; commits: 87f9938)
- [GT-JEMALLOC-5.3.1-0143] Fixed off-by-one bug in stats_arenas_i_bins_j and stats_arenas_i_extents_j bounds checks, preventing array out-of-bounds access, and added unit test validating bounds index returns ENOENT. (PRs: #2873; commits: eab2b29)
- [GT-JEMALLOC-5.3.1-0144] Fixed the fallback value error when sysconf failed in the os_page_detect function, and changed the wrong LG_PAGE to the correct PAGE to avoid the page size being set to a very small value. (PRs: #2873; commits: dd30c91)
- [GT-JEMALLOC-5.3.1-0145] Fixed the problem in prof_stack_range that the error check failed due to the wrong return value type of malloc_read_fd (using size_t instead of ssize_t), and adjusted the error handling logic to correctly distinguish between read failure and read end. (PRs: #2873; commits: 3f6e63e)
- [GT-JEMALLOC-5.3.1-0146] Fixed an issue where using the wrong variable in an array index loop resulted in array entries not being initialized correctly. (PRs: #2873; commits: 234404d)
- [GT-JEMALLOC-5.3.1-0147] Fixed the wrong order of edata_init calling parameters in the extent_alloc_dss function, replacing the redundant size parameter with the correct slab parameter. (PRs: #2873; commits: 2fceece)
- [GT-JEMALLOC-5.3.1-0176] Fix Cirrus CI. (commits: 6d181bc)

### Build and CI

- [GT-JEMALLOC-5.3.1-0169] Fixed a compilation issue caused by searching the math library libm under MSVC 2022, skipping the libm search when MSVC is detected. (PRs: #2720; commits: 734f29c)
- [GT-JEMALLOC-5.3.1-0170] Temporarily removed Windows build configurations in Travis CI due to infrastructure failure. (PRs: #2864; commits: 755735a)
- [GT-JEMALLOC-5.3.1-0172] Remove Cirrus CI (commits: c7690e9)
- [GT-JEMALLOC-5.3.1-0173] Remove --enable-limit-usize-gap for cirrus CI since the config-time option is removed. (commits: e350c71)
- [GT-JEMALLOC-5.3.1-0174] Remove unsupported Cirrus CI config (commits: f55e0c3)
- [GT-JEMALLOC-5.3.1-0175] Limit Cirrus CI to freebsd 15 and 14 (commits: e29ac61)
- [GT-JEMALLOC-5.3.1-0177] Test on more FreeBSD versions (commits: d284aad)
- [GT-JEMALLOC-5.3.1-0178] CI update FreeBSD version. (commits: a9215bf)

### Documentation

- [GT-JEMALLOC-5.3.1-0067] Update Windows building instructions. (@Lapenkov: 37139328) (PRs: #2292; commits: 3713932)
- [GT-JEMALLOC-5.3.1-0068] Add vcpkg installation instructions. (@LilyWangLL: c0c9783e) (commits: c0c9783)

### Functional Changes / Refactorings

- [GT-JEMALLOC-5.3.1-0157] Roll back the peak demand tracking function and remove related initialization code and functions. (commits: 27d7960)
- [GT-JEMALLOC-5.3.1-0158] Roll back PR #2608, revert the jemalloc changes of the Meta branch, including adjustments to arena initialization, bin information configuration and tcache default settings. (PRs: #2608, #2707, #2864; commits: 2114349)
- [GT-JEMALLOC-5.3.1-0159] Changed malloc_write_fd and malloc_read_fd from static inline functions to non-inline global functions, and added a retry loop to handle partial writes and reads. (PRs: #2864; commits: 38b1242)

### New Features

- [GT-JEMALLOC-5.3.1-0089] Added processing of opt.cache_oblivious option in configuration parsing. (PRs: #2307; commits: a1c7d9c)
- [GT-JEMALLOC-5.3.1-0090] Added filtering for internal functions such as je_malloc_default and do_rallocx in the jeprof tool to streamline performance analysis output. (PRs: #2452, #2692; commits: 397827a, c1d3ad4)
- [GT-JEMALLOC-5.3.1-0091] Added separate statistics for edata and rtree memory allocation, and introduced the base_alloc_rtree function for rtree node allocation. (PRs: #2551; commits: 36becb1)
- [GT-JEMALLOC-5.3.1-0092] A new batcher module is added, which is used to cache simple operation commands in batches for subsequent use by other threads. (PRs: #2608; commits: 70c94d7)

### Performance

- [GT-JEMALLOC-5.3.1-0054] Enable tcache for deallocation-only threads. (@interwq: 143e9c4a) (PRs: #2349; commits: 143e9c4)
- [GT-JEMALLOC-5.3.1-0055] Inline to accelerate operator delete. (@guangli-dai: e8f9f138) (PRs: #2332; commits: e8f9f13)
- [GT-JEMALLOC-5.3.1-0056] Optimize pairing heap's performance. (@deadalnix: 5266152d, be6da4f6, 543e2d61, 10d71315, 92aa52c0, @Svetlitski: 36ca0c1b) (PRs: #2389, #2391, #2393, #2481, #2563, #2565; commits: 10d7131, 36ca0c1, 5266152, 543e2d6, 92aa52c, be6da4f)
- [GT-JEMALLOC-5.3.1-0058] Optimize a hot function `edata_cmp_summary_comp` to accelerate it. (@Svetlitski: 6841110b, @guangli-dai: 0181aaa4) (PRs: #2423, #2714; commits: 0181aaa, 6841110)
- [GT-JEMALLOC-5.3.1-0060] Allow oversize arena not to purge immediately when background threads are enabled, although the default decay time is 0 to be back compatible. (@interwq: d1313313) (PRs: #2466; commits: d131331)
- [GT-JEMALLOC-5.3.1-0062] Optimize fast path to allow static size class computation. (@interwq: 323ed2e3) (PRs: #2708; commits: 323ed2e)
- [GT-JEMALLOC-5.3.1-0064] Reduce the arena switching overhead by avoiding forced purging when background thread is enabled. (@interwq: a3910b98) (PRs: #2840; commits: a3910b9)
- [GT-JEMALLOC-5.3.1-0065] Improve the reuse efficiency by limiting the maximum coalesced size for large extents. (@jiebinn: 3c14707b) (PRs: #2842; commits: 3c14707)
- [GT-JEMALLOC-5.3.1-0162] Use local variables to set the alignment of specific memory allocations to avoid unnecessary alignment and memory fragmentation caused by permanently modifying mmap_flags. (PRs: #2456; commits: 5832ef6)
- [GT-JEMALLOC-5.3.1-0163] Replace all integer-to-pointer conversions that suppress optimizations with equivalent operations that preserve pointer source information, and enable clang-tidy checks to prevent such problems in the future. (PRs: #2481, #2485; commits: 3e82f35)
- [GT-JEMALLOC-5.3.1-0164] Use the assume built-in function provided by the compiler to replace the original unreachable implementation to express assumptions more reliably and avoid potential performance problems. (PRs: #2510; commits: 4f50f78)
- [GT-JEMALLOC-5.3.1-0165] Optimized the alignment and locality of bins and their mutex locks in arena, and adjusted the memory allocation layout to improve performance. (PRs: #2560; commits: 3025b02)
- [GT-JEMALLOC-5.3.1-0166] Optimize the lock competition when tcache is refreshed to arena bin: partition by bin before locking, avoid full array scan when lock is held, and know the number to be refreshed in advance. (PRs: #2608; commits: 44d91cf)
- [GT-JEMALLOC-5.3.1-0167] Change the atomic operation of accessing the process madvise pid file descriptor from sequential consistency to relaxed atomic operation to improve performance. (PRs: #2864; commits: 9528a2e)

### Security

- [GT-JEMALLOC-5.3.1-0168] Fixed the stack out-of-bounds writing vulnerability caused by incorrect use of the address operator in background_thread.c, and the out-of-bounds writing vulnerability in malloc_vsnprintf when size is 0, and added relevant unit tests. (PRs: #59, #2864, #2873; commits: 5f353dc, c2d5704)
