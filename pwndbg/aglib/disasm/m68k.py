from capstone import *  # noqa: F403
from capstone.m68k import *  # noqa: F403

import pwndbg.aglib.disasm.arch

class M68kDisassemblyAssistant(pwndbg.aglib.disasm.arch.DisassemblyAssistant):
    def __init__(self, architecture) -> None:
        super().__init__(architecture)

    # TODO: put funny stuff here