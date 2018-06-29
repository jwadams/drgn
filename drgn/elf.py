# Copyright 2018 - Omar Sandoval
# SPDX-License-Identifier: GPL-3.0+

from collections import namedtuple
import struct
from typing import Dict, List, NamedTuple, Optional, Tuple, Union


# Automatically generated from elf.h
EI_NIDENT = (16)
EI_MAG0 = 0
ELFMAG0 = 0x7f
EI_MAG1 = 1
ELFMAG1 = 0x45
EI_MAG2 = 2
ELFMAG2 = 0x4c
EI_MAG3 = 3
ELFMAG3 = 0x46
EI_CLASS = 4
ELFCLASSNONE = 0
ELFCLASS32 = 1
ELFCLASS64 = 2
ELFCLASSNUM = 3
EI_DATA = 5
ELFDATANONE = 0
ELFDATA2LSB = 1
ELFDATA2MSB = 2
ELFDATANUM = 3
EI_VERSION = 6
EI_OSABI = 7
EI_ABIVERSION = 8
EI_PAD = 9
EV_NONE = 0
EV_CURRENT = 1
EV_NUM = 2
SHN_UNDEF = 0
SHN_LORESERVE = 0xff00
SHN_LOPROC = 0xff00
SHN_BEFORE = 0xff00
SHN_AFTER = 0xff01
SHN_HIPROC = 0xff1f
SHN_LOOS = 0xff20
SHN_HIOS = 0xff3f
SHN_ABS = 0xfff1
SHN_COMMON = 0xfff2
SHN_XINDEX = 0xffff
SHN_HIRESERVE = 0xffff
SHT_NULL = 0
SHT_PROGBITS = 1
SHT_SYMTAB = 2
SHT_STRTAB = 3
SHT_RELA = 4
SHT_HASH = 5
SHT_DYNAMIC = 6
SHT_NOTE = 7
SHT_NOBITS = 8
SHT_REL = 9
SHT_SHLIB = 10
SHT_DYNSYM = 11
SHT_INIT_ARRAY = 14
SHT_FINI_ARRAY = 15
SHT_PREINIT_ARRAY = 16
SHT_GROUP = 17
SHT_SYMTAB_SHNDX = 18
SHT_NUM = 19
SHT_LOOS = 0x60000000
SHT_GNU_ATTRIBUTES = 0x6ffffff5
SHT_GNU_HASH = 0x6ffffff6
SHT_GNU_LIBLIST = 0x6ffffff7
SHT_CHECKSUM = 0x6ffffff8
SHT_LOSUNW = 0x6ffffffa
SHT_SUNW_move = 0x6ffffffa
SHT_SUNW_COMDAT = 0x6ffffffb
SHT_SUNW_syminfo = 0x6ffffffc
SHT_GNU_verdef = 0x6ffffffd
SHT_GNU_verneed = 0x6ffffffe
SHT_GNU_versym = 0x6fffffff
SHT_HISUNW = 0x6fffffff
SHT_HIOS = 0x6fffffff
SHT_LOPROC = 0x70000000
SHT_HIPROC = 0x7fffffff
SHT_LOUSER = 0x80000000
SHT_HIUSER = 0x8fffffff
SHN_MIPS_ACOMMON = 0xff00
SHN_MIPS_TEXT = 0xff01
SHN_MIPS_DATA = 0xff02
SHN_MIPS_SCOMMON = 0xff03
SHN_MIPS_SUNDEFINED = 0xff04
SHT_MIPS_LIBLIST = 0x70000000
SHT_MIPS_MSYM = 0x70000001
SHT_MIPS_CONFLICT = 0x70000002
SHT_MIPS_GPTAB = 0x70000003
SHT_MIPS_UCODE = 0x70000004
SHT_MIPS_DEBUG = 0x70000005
SHT_MIPS_REGINFO = 0x70000006
SHT_MIPS_PACKAGE = 0x70000007
SHT_MIPS_PACKSYM = 0x70000008
SHT_MIPS_RELD = 0x70000009
SHT_MIPS_IFACE = 0x7000000b
SHT_MIPS_CONTENT = 0x7000000c
SHT_MIPS_OPTIONS = 0x7000000d
SHT_MIPS_SHDR = 0x70000010
SHT_MIPS_FDESC = 0x70000011
SHT_MIPS_EXTSYM = 0x70000012
SHT_MIPS_DENSE = 0x70000013
SHT_MIPS_PDESC = 0x70000014
SHT_MIPS_LOCSYM = 0x70000015
SHT_MIPS_AUXSYM = 0x70000016
SHT_MIPS_OPTSYM = 0x70000017
SHT_MIPS_LOCSTR = 0x70000018
SHT_MIPS_LINE = 0x70000019
SHT_MIPS_RFDESC = 0x7000001a
SHT_MIPS_DELTASYM = 0x7000001b
SHT_MIPS_DELTAINST = 0x7000001c
SHT_MIPS_DELTACLASS = 0x7000001d
SHT_MIPS_DWARF = 0x7000001e
SHT_MIPS_DELTADECL = 0x7000001f
SHT_MIPS_SYMBOL_LIB = 0x70000020
SHT_MIPS_EVENTS = 0x70000021
SHT_MIPS_TRANSLATE = 0x70000022
SHT_MIPS_PIXIE = 0x70000023
SHT_MIPS_XLATE = 0x70000024
SHT_MIPS_XLATE_DEBUG = 0x70000025
SHT_MIPS_WHIRL = 0x70000026
SHT_MIPS_EH_REGION = 0x70000027
SHT_MIPS_XLATE_OLD = 0x70000028
SHT_MIPS_PDR_EXCEPTION = 0x70000029
SHN_PARISC_ANSI_COMMON = 0xff00
SHN_PARISC_HUGE_COMMON = 0xff01
SHT_PARISC_EXT = 0x70000000
SHT_PARISC_UNWIND = 0x70000001
SHT_PARISC_DOC = 0x70000002
SHT_ALPHA_DEBUG = 0x70000001
SHT_ALPHA_REGINFO = 0x70000002
SHT_ARM_EXIDX = (SHT_LOPROC + 1)
SHT_ARM_PREEMPTMAP = (SHT_LOPROC + 2)
SHT_ARM_ATTRIBUTES = (SHT_LOPROC + 3)
SHT_IA_64_EXT = (SHT_LOPROC + 0)
SHT_IA_64_UNWIND = (SHT_LOPROC + 1)


class ElfFormatError(Exception):
    pass


class Elf_Ehdr(NamedTuple):
    e_ident: bytes
    e_type: int
    e_machine: int
    e_version: int
    e_entry: int
    e_phoff: int
    e_shoff: int
    e_flags: int
    e_ehsize: int
    e_phentsize: int
    e_phnum: int
    e_shentsize: int
    e_shnum: int
    e_shstrndx: int


class Elf_Shdr(NamedTuple):
    sh_name: int
    sh_type: int
    sh_flags: int
    sh_addr: int
    sh_offset: int
    sh_size: int
    sh_link: int
    sh_info: int
    sh_addralign: int
    sh_entsize: int
    name: str


class Elf_Sym(NamedTuple):
    st_name: int
    st_info: int
    st_other: int
    st_shndx: int
    st_value: int
    st_size: int


class ElfFile:
    def __init__(self, path: str, data: bytes) -> None:
        self.path = path
        self.data = data
        self.ehdr = self._ehdr()
        self.shdrs = self._shdrs()
        self.sections = {shdr.name: shdr for shdr in self.shdrs}
        self._symbols: Optional[Dict[str, List[Elf_Sym]]] = None

    def _ehdr(self) -> Elf_Ehdr:
        if (self.data[EI_MAG0] != ELFMAG0 or self.data[EI_MAG1] != ELFMAG1 or
                self.data[EI_MAG2] != ELFMAG2 or self.data[EI_MAG3] != ELFMAG3):
            raise ValueError('not an ELF file')

        if self.data[EI_VERSION] != EV_CURRENT:
            raise ValueError('ELF version is not EV_CURRENT')

        if self.data[EI_DATA] == ELFDATA2LSB:
            fmt = '<'
        elif self.data[EI_DATA] == ELFDATA2MSB:
            fmt = '>'
        else:
            raise ValueError(f'unknown ELF data encoding {self.data[EI_DATA]}')

        if self.data[EI_CLASS] == ELFCLASS64:
            fmt += '16sHHLQQQLHHHHHH'
        elif self.data[EI_CLASS] == ELFCLASS32:
            raise NotImplementedError('32-bit ELF is not implemented')
        else:
            raise ValueError(f'unknown ELF class {self.data[EI_CLASS]}')
        return Elf_Ehdr._make(struct.unpack_from(fmt, self.data))

    def _shdrs(self) -> List[Elf_Shdr]:
        if self.ehdr.e_ident[EI_DATA] == ELFDATA2LSB:
            fmt = '<'
        else:
            fmt = '>'

        if self.ehdr.e_ident[EI_CLASS] == ELFCLASS64:
            fmt += 'LLQQQQLLQQ'
        else:
            assert False

        # TODO: e_shnum == 0
        buf = self.data[self.ehdr.e_shoff:
                        self.ehdr.e_shoff + self.ehdr.e_shnum * self.ehdr.e_shentsize]
        raw_shdrs = list(struct.iter_unpack(fmt, buf))

        if self.ehdr.e_shstrndx == SHN_UNDEF:
            raise ValueError('no string table index in ELF header')
        elif self.ehdr.e_shstrndx == SHN_XINDEX:
            sh_link = raw_shdrs[0][6]
            shstrtab_shdr = raw_shdrs[sh_link]
        else:
            if self.ehdr.e_shstrndx >= SHN_LORESERVE:
                raise ValueError('invalid string table index in ELF header')
            shstrtab_shdr = raw_shdrs[self.ehdr.e_shstrndx]
        sh_offset = shstrtab_shdr[4]
        sh_size = shstrtab_shdr[5]
        shstrtab = bytes(self.data[sh_offset:sh_offset + sh_size])

        shdrs = []
        for raw_shdr in raw_shdrs:
            sh_name = raw_shdr[0]
            if sh_name:
                end = shstrtab.index(b'\0', sh_name)
                section_name = shstrtab[sh_name:end].decode()
            else:
                section_name = ''
            # mypy claims 'Too many arguments for "Elf_Shdr"'
            shdrs.append(Elf_Shdr(*raw_shdr, section_name)) # type: ignore
        return shdrs

    @property
    def symbols(self) -> Dict[str, List[Elf_Sym]]:
        if self._symbols is None:
            if self.ehdr.e_ident[EI_DATA] == ELFDATA2LSB:
                fmt = '<'
            else:
                fmt = '>'

            if self.ehdr.e_ident[EI_CLASS] == ELFCLASS64:
                fmt += 'LBBHQQ'
            else:
                assert False

            shdr = self.sections['.symtab']
            buf = self.data[shdr.sh_offset:shdr.sh_offset + shdr.sh_size]
            symtab = [Elf_Sym._make(sym) for sym in struct.iter_unpack(fmt, buf)]

            strtab_shdr = self.sections['.strtab']
            strtab = bytes(self.data[strtab_shdr.sh_offset:
                                     strtab_shdr.sh_offset + strtab_shdr.sh_size])
            symbols: Dict[str, List[Elf_Sym]] = {}
            for sym in symtab:
                if not sym.st_name:
                    continue
                end = strtab.index(b'\0', sym.st_name)
                symbol_name = strtab[sym.st_name:end].decode()
                try:
                    symbols[symbol_name].append(sym)
                except KeyError:
                    symbols[symbol_name] = [sym]
            self._symbols = symbols
        return self._symbols