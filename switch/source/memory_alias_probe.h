#pragma once

#include <switch/types.h>
#include <cstdint>

namespace switch_memory_probe
{
    struct MemorySnapshot
    {
        Result query = 0xFFFFFFFFu;
        uint32_t appletType = 0;
        uint64_t currentBytes = 0;
        uint64_t limitBytes = 0;
        bool available = false;
    };

    MemorySnapshot ReadMemorySnapshot();

    struct ResultInfo
    {
        Result reserve = 0xFFFFFFFFu;
        Result create = 0xFFFFFFFFu;
        Result map[3]{0xFFFFFFFFu, 0xFFFFFFFFu, 0xFFFFFFFFu};
        Result commit = 0xFFFFFFFFu;
        bool coherent = false;
        bool available = false;
    };

    ResultInfo Run();
}
