# Ground Truth for jemalloc-5.0.1-5.1.0

## Important Changes

### Allocation Policy & Management Layer

- [GT-JEMALLOC-5.1.0-0043] Refactor extent management with dumpable flag. (@davidtgoldblatt) (PRs: #1052, #1076; commits: 211b1f3, 26a8f82, bbaa724, d14bbf8)
- [GT-JEMALLOC-5.1.0-0044] Add runtime detection of lazy purging. (@interwq) (PRs: #1034, #1048; commits: 0720192, 31ab38b)
- [GT-JEMALLOC-5.1.0-0049] Fast division by dynamic values. (@davidtgoldblatt) (PRs: #1095; commits: 21f7c13, d41b19f)
- [GT-JEMALLOC-5.1.0-0072] Separated bin management-related types, functions, global arrays, and initialization and fork processing logic from the arena module into independent bin modules, and renamed related types and global arrays. (Architecture event: bin module separation) (PRs: #1093; commits: 48bb4a0, 4bf4a1c, a8dd887)
- [GT-JEMALLOC-5.1.0-0073] Migrate the bin statistics related code from the arena module to the bin module, and add the bin_stats_merge function. (Architecture event: jemalloc_Core_Internal module change) (PRs: #1093; commits: 8aafa27)
- [GT-JEMALLOC-5.1.0-0075] Relax the reentrancy constraints of extent hooks, remove non-arena 0 assertions, and add reentrancy level upper limit checks. (Architecture-related: public API) (PRs: #1010; commits: a315688)

### Architecture-related Changes

- [GT-JEMALLOC-5.1.0-0092] The build system now allows the toolchain to determine the nm tool path by itself, ensuring that the symbol list is generated correctly when cross-compiling. (Architecture-related: build and installation methods) (PRs: #949, #1024; commits: 24766cc, 3f50493)
- [GT-JEMALLOC-5.1.0-0093] Fixed the problem of symbol list failure due to lack of dumpbin tool in MinGW environment. Now only dumpbin is used for symbol export on Cygwin platform. (Architecture-related: platform compatibility) (PRs: #949, #1024; commits: a545f18, ef55006)

### Cross-cutting / Other Architecture-related Changes

- [GT-JEMALLOC-5.1.0-0005] Allow arena index lookup based on allocation addresses via mallctl. (@lionkov)
- [GT-JEMALLOC-5.1.0-0006] Allow disabling initial-exec TLS model. (@davidtgoldblatt, @KenMacD) (PRs: #1180; commits: a62e42b)
- [GT-JEMALLOC-5.1.0-0018] Support GNU/kFreeBSD configuration. (@paravoid) (PRs: #959, #985; commits: 0975b88, 8da69b6)
- [GT-JEMALLOC-5.1.0-0019] Support m68k, nios2 and SH3 architectures. (@paravoid) (PRs: #985, #807554, #816236, #863424; commits: 82d1a3f)
- [GT-JEMALLOC-5.1.0-0020] Fall back to FD_CLOEXEC when O_CLOEXEC is unavailable. (@zonyitoo) (PRs: #959, #985; commits: 0975b88, 8da69b6)
- [GT-JEMALLOC-5.1.0-0021] Fix symbol listing for cross-compiling. (@tamird) (PRs: #1211; commits: b73380b)
- [GT-JEMALLOC-5.1.0-0024] Fix MSVC 2015 & 2017 builds. (@rustyx) (PRs: #1053; commits: 33df2fa)
- [GT-JEMALLOC-5.1.0-0025] Improve RISC-V support. (@EdSchouten) (PRs: #972, #1081, #1096; commits: 1ab2ab2, 749caf1, ba5992f)
- [GT-JEMALLOC-5.1.0-0026] Set name mangling script in strict mode. (@nicolov)
- [GT-JEMALLOC-5.1.0-0029] Make sure CXXFLAGS is tested with CPP compiler. (@nehaljwani) (PRs: #1101; commits: 78a87e4)
- [GT-JEMALLOC-5.1.0-0030] Fix 32-bit build on MSVC. (@rustyx) (PRs: #1053, #1193, #1206, #1207, #1211; commits: 33df2fa, 4c8829e, 63712b4, 6df9060, b001e6e, b73380b)
- [GT-JEMALLOC-5.1.0-0033] Add configure option --disable-initial-exec-tls which can allow jemalloc to be dynamically loaded after program startup. (@davidtgoldblatt, @KenMacD) (PRs: #1180; commits: a62e42b)
- [GT-JEMALLOC-5.1.0-0034] AArch64: Add ILP32 support. (@cmuellner) (PRs: #1193, #1206, #1207; commits: 4c8829e, 63712b4, 6df9060, b001e6e)
- [GT-JEMALLOC-5.1.0-0035] Add --with-lg-vaddr configure option to support cross compiling. (@cmuellner, @davidtgoldblatt) (PRs: #1180, #1193, #1206, #1207; commits: 4c8829e, 63712b4, 6df9060, a62e42b, b001e6e)
- [GT-JEMALLOC-5.1.0-0041] Add internal fine-grained logging functionality for debugging use. (@davidtgoldblatt) (PRs: #958, #962, #964; commits: 9761b44, a9f7732, e215a7b, e6aeceb)
- [GT-JEMALLOC-5.1.0-0057] Validate returned file descriptor before use. (@zonyitoo) (PRs: #959, #961, #985, #1076; commits: 0975b88, 26a8f82, 8da69b6, aa6c282)
- [GT-JEMALLOC-5.1.0-0067] Fix include path order for out-of-tree builds. (@cmuellner) (PRs: #1211; commits: b73380b)
- [GT-JEMALLOC-5.1.0-0069] Remove mallctl interfaces: (PRs: #1048, #1110, #1134; commits: 548153e, efa4053, f4f814c)

### User-Facing Interface Layer

- [GT-JEMALLOC-5.1.0-0001] Implement transparent huge page support for internal metadata. (@interwq) (PRs: #983, #998, #1046, #1134; commits: 47b20bb, 79e8345, 8fdd9a5, e4f090e, e55c3ca)
- [GT-JEMALLOC-5.1.0-0002] Add opt.thp to allow enabling / disabling transparent huge pages for all mappings. (@interwq) (PRs: #983, #998, #1046, #1134; commits: 47b20bb, 79e8345, 8fdd9a5, e4f090e, e55c3ca)
- [GT-JEMALLOC-5.1.0-0003] Add maximum background thread count option. (@djwatson) (PRs: #1156; commits: 8b14f3a)
- [GT-JEMALLOC-5.1.0-0004] Allow prof_active to control opt.lg_prof_interval and prof.gdump. (@interwq) (PRs: #1160; commits: 2dccf45)
- [GT-JEMALLOC-5.1.0-0007] Add opt.lg_extent_max_active_fit to set the max ratio between the size of the active extent selected (to split off from) and the size of the requested allocation. (@interwq, @davidtgoldblatt) (PRs: #1071; commits: fac7068)
- [GT-JEMALLOC-5.1.0-0008] Add retain_grow_limit to set the max size when growing virtual address space. (@interwq) (PRs: #1035, #1064, #1096; commits: 7a8bc71, ba5992f, e422fa8)
- [GT-JEMALLOC-5.1.0-0009] Add mallctl interfaces: (PRs: #987, #1158, #1182, #1194; commits: a32b7bd, b082535, cf2f4aa, e40b2f7)
- [GT-JEMALLOC-5.1.0-0010] arena.<i>.retain_grow_limit (@interwq) (PRs: #989, #1093, #1172; commits: 0258542, 7f1b02e, 9c05490)
- [GT-JEMALLOC-5.1.0-0011] arenas.lookup (@lionkov) (PRs: #1194; commits: a32b7bd)
- [GT-JEMALLOC-5.1.0-0013] opt.lg_extent_max_active_fit (@interwq) (PRs: #1071, #1089; commits: 5e03328, fac7068)
- [GT-JEMALLOC-5.1.0-0015] opt.metadata_thp (@interwq) (PRs: #983, #998, #1046, #1134; commits: 47b20bb, 79e8345, 8fdd9a5, e4f090e, e55c3ca)
- [GT-JEMALLOC-5.1.0-0016] opt.thp (@interwq) (PRs: #983, #998, #1046, #1134; commits: 47b20bb, 79e8345, 8fdd9a5, e4f090e, e55c3ca)
- [GT-JEMALLOC-5.1.0-0022] Fix high bits computation on ARM. (@davidtgoldblatt, @paravoid) (PRs: #1035; commits: 7a8bc71)
- [GT-JEMALLOC-5.1.0-0023] Disable the CPU_SPINWAIT macro for Power. (@davidtgoldblatt, @marxin) (commits: 1245faa)
- [GT-JEMALLOC-5.1.0-0027] Avoid MADV_HUGEPAGE on ARM. (@marxin) (PRs: #983, #998, #1046, #1134; commits: 47b20bb, 79e8345, 8fdd9a5, e4f090e, e55c3ca)
- [GT-JEMALLOC-5.1.0-0028] Modify configure to determine return value of strerror_r. (@davidtgoldblatt, @cferris1000) (PRs: #1109; commits: f78d4ca)
- [GT-JEMALLOC-5.1.0-0031] Fix external symbol on MSVC. (@maksqwe) (PRs: #980, #1053; commits: 048c667, 33df2fa)
- [GT-JEMALLOC-5.1.0-0032] Avoid a printf format specifier warning. (@jasone) (PRs: #1177; commits: 2a80d6f)
- [GT-JEMALLOC-5.1.0-0036] Improve active extent fit with extent_max_active_fit. This considerably reduces fragmentation over time and improves virtual memory and metadata usage. (@davidtgoldblatt, @interwq) (PRs: #1071; commits: fac7068)
- [GT-JEMALLOC-5.1.0-0037] Eagerly coalesce large extents to reduce fragmentation. (@interwq) (PRs: #1071; commits: 3e64dae, fac7068)
- [GT-JEMALLOC-5.1.0-0039] Avoid attempting new mappings for in place expansion with retain, since it rarely succeeds in practice and causes high overhead. (@interwq) (PRs: #983, #998, #1046, #1134; commits: 47b20bb, 79e8345, 8fdd9a5, e4f090e, e55c3ca)
- [GT-JEMALLOC-5.1.0-0042] Refactor arena / tcache interactions. (@davidtgoldblatt) (PRs: #989, #1093; commits: 901d94a, 9c05490, f3170ba)
- [GT-JEMALLOC-5.1.0-0048] Make decay to always purge one more extent than before, because in practice large extents are usually the ones that cross the decay threshold. Purging the additional extent helps save memory as well as reduce VM fragmentation. (@interwq) (PRs: #1071, #1092; commits: 740bdd6, fac7068)
- [GT-JEMALLOC-5.1.0-0053] Convert stats printing to use a structured text emitter. (@davidtgoldblatt) (PRs: #1144; commits: 07fb707, 0d20eda, 4a335e0, 4c36cd2, 4eed989, 8076b28, 86c61d4, 8fc8506, 9e1846b, a1738f4, a6ef061, b646f89, bc6620f, cbde666, e5acc35, ec31d47)
- [GT-JEMALLOC-5.1.0-0056] Fix deadlock with multithreaded fork in OS X. (@davidtgoldblatt) (PRs: #895, #954; commits: 0a4f5a7, fb6787a)
- [GT-JEMALLOC-5.1.0-0060] Fix potentially unbound increase during decay, caused by one thread keep stashing memory to purge while other threads generating new pages. The number of pages to purge is checked to prevent this. (@interwq) (PRs: #1069; commits: b5d071c)
- [GT-JEMALLOC-5.1.0-0062] Handle 32 bit mutex counters. (@rkmisra) (PRs: #1100; commits: f47e39d)
- [GT-JEMALLOC-5.1.0-0074] Introduce the emitter module, support structured output (JSON/table), and enhance the row-level output and title printing functions of table mode. (Architecture events: The core internal module adds the emitter module) (PRs: #1144; commits: 27a8fe6, ebe0b5f)
- [GT-JEMALLOC-5.1.0-0076] Allows setting extent hooks on uninitialized automatic arena. If the automatic arena has not been initialized, its initialization will be triggered. (Architecture-related: extent hooks setting behavior) (PRs: #1173; commits: 3f0dc64)
- [GT-JEMALLOC-5.1.0-0078] Fix the regression problem of cache bin queue not being cleared after fork and reinitializing it in the child process. (Architecture-related: platform compatibility) (PRs: #1020; commits: 9b20a4b)
- [GT-JEMALLOC-5.1.0-0079] Fix -Wshift-negative-value warning caused by left-shifting negative values. (Architecture-related: public API) (PRs: #1029; commits: 3959a9f)
- [GT-JEMALLOC-5.1.0-0080] Capitalize the log macro name to avoid conflict with the logarithmic function name in math.h. (Architecture-related: public API) (PRs: #1041; commits: 8a7ee30)
- [GT-JEMALLOC-5.1.0-0081] In the iallocztm function, check the lock level only in non-reentrant state. (Architecture-related: core allocator behavior) (PRs: #1097; commits: 91b247d)
- [GT-JEMALLOC-5.1.0-0082] Fixed the read/write function return type warning on the Windows platform and added a new encapsulation function. (Architecture-related: platform compatibility) (commits: d3e0976)

## Routine Changes

### Bug Fixes

- [GT-JEMALLOC-5.1.0-0083] Fix test/unit/pages test to use runtime variable checking for MADV_HUGEPAGE support instead. (PRs: #986, #1017; commits: 3ec279b, 886053b)
- [GT-JEMALLOC-5.1.0-0084] Fix compilation warning caused by missing fields in rtree cache initializer. (PRs: #1022; commits: d60f3ba)
- [GT-JEMALLOC-5.1.0-0085] Delay background_thread_ctl_init execution and add lock-free assertion. (PRs: #1047; commits: a2e6eb2)
- [GT-JEMALLOC-5.1.0-0086] Fixed synchronization issues and statistical corrections when switching to THP in automatic mode of the base allocator. (PRs: #1068; commits: cb3b72b)
- [GT-JEMALLOC-5.1.0-0087] Avoid incorrectly setting zero and commit flags when split fails in extent_recycle. (PRs: #1075; commits: e475d03)
- [GT-JEMALLOC-5.1.0-0088] Fix issue with incorrectly adjusting gdump counts on leak paths. (PRs: #1084; commits: 955b1d9)
- [GT-JEMALLOC-5.1.0-0089] Add a check to see if tsdn is empty before reading the reentrancy level. (PRs: #1097; commits: 41790f4)
- [GT-JEMALLOC-5.1.0-0090] Fix the resource leak problem in the path where extent split fails. (PRs: #1181; commits: c95284d)
- [GT-JEMALLOC-5.1.0-0091] Remove false assertions, allowing background threads to be created lazily in a paused state. (PRs: #1185; commits: b8f4c73)
- [GT-JEMALLOC-5.1.0-0094] Fix MSVC build (commits: a3abbb4)

### Documentation

- [GT-JEMALLOC-5.1.0-0071] Add TUNING.md. (@interwq, @davidtgoldblatt, @djwatson) (PRs: #1179; commits: 2e7af1a)

### Functional Changes / Refactorings

- [GT-JEMALLOC-5.1.0-0068] Remove --disable-thp. (@interwq) (PRs: #1179; commits: 3bcaede)

### New Features

- [GT-JEMALLOC-5.1.0-0012] max_background_threads (@djwatson)
- [GT-JEMALLOC-5.1.0-0014] opt.max_background_threads (@djwatson)
- [GT-JEMALLOC-5.1.0-0017] stats.metadata_thp (@interwq)
- [GT-JEMALLOC-5.1.0-0077] Filter out newImpl functions in profiling output. (PRs: #968; commits: 2d2fa72)

### Other Changes

- [GT-JEMALLOC-5.1.0-0070] config.thp (@interwq) (PRs: #1134; commits: efa4053)

### Performance

- [GT-JEMALLOC-5.1.0-0038] sdallocx: only read size info when page aligned (i.e. possibly sampled), which speeds up the sized deallocation path significantly. (@interwq) (PRs: #972; commits: 1ab2ab2)
- [GT-JEMALLOC-5.1.0-0040] Refactor OOM handling in newImpl. (@wqfish) (PRs: #963; commits: b28f31e)
- [GT-JEMALLOC-5.1.0-0045] Use pairing heap instead of red-black tree for extents_avail. (@djwatson) (PRs: #888, #1039; commits: 7c6c99b)
- [GT-JEMALLOC-5.1.0-0046] Use sysctl on startup in FreeBSD. (@trasz) (PRs: #1061; commits: 9f455e2, d591df0)
- [GT-JEMALLOC-5.1.0-0047] Use thread local prng state instead of atomic. (@djwatson) (PRs: #852, #1070; commits: d6feed6)
- [GT-JEMALLOC-5.1.0-0050] Improve the fit for aligned allocation. (@interwq, @edwinsmith) (PRs: #1096; commits: ba5992f)
- [GT-JEMALLOC-5.1.0-0051] Refactor extent_t bitpacking. (@rkmisra) (PRs: #1103; commits: 72bdbc3)
- [GT-JEMALLOC-5.1.0-0052] Optimize the generated assembly for ticker operations. (@davidtgoldblatt)
- [GT-JEMALLOC-5.1.0-0054] Remove preserve_lru feature for extents management. (@djwatson) (PRs: #1154; commits: 6d02421)
- [GT-JEMALLOC-5.1.0-0055] Consolidate two memory loads into one on the fast deallocation path. (@davidtgoldblatt, @interwq) bug fixes (most of the issues are only relevant to jemalloc 5.0): (PRs: #1157; commits: 4be74d5)
- [GT-JEMALLOC-5.1.0-0058] Fix a few background thread initialization and shutdown issues. (@interwq) (PRs: #1155, #1171; commits: 21eb0d1, dedfeec)
- [GT-JEMALLOC-5.1.0-0059] Fix an extent coalesce + decay race by taking both coalescing extents off the LRU list. (@interwq) (PRs: #1071; commits: eb1b08d)
- [GT-JEMALLOC-5.1.0-0061] Fix a FreeBSD bootstrap assertion. (@strejda, @interwq)
- [GT-JEMALLOC-5.1.0-0063] Fix a indexing bug when creating background threads. (@davidtgoldblatt, @binliu19) (PRs: #1140; commits: 26b1c13)
- [GT-JEMALLOC-5.1.0-0064] Fix arguments passed to extent_init. (@yuleniwo, @interwq) (PRs: #1159; commits: 4df483f)
- [GT-JEMALLOC-5.1.0-0065] Fix addresses used for ordering mutexes. (@rkmisra) (PRs: #1165; commits: 5f51882)
- [GT-JEMALLOC-5.1.0-0066] Fix abort_conf processing during bootstrap. (@interwq) (PRs: #987, #1182; commits: b082535, e40b2f7)
