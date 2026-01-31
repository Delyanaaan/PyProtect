import sys

from pathlib import Path
from contextlib import suppress
from src.tools import ToolsConsole, Arguments
from src.obfuscator import Obfuscator


if __name__ == "__main__":
    with suppress(KeyboardInterrupt):
        with suppress(IndexError):
            one = sys.argv[1].lower()

            if one in ("--help", "-h"):
                raise IndexError()

            if not ToolsConsole.validate_args(sys.argv[1:]):
                ToolsConsole.error("Invalid arguments provided.\n")
                raise IndexError()
            
            input_file = None
            output_file = None
            obf_method = None
            compress = False

            for i, arg in enumerate(sys.argv):
                if arg in ("--input", "-in"):
                    input_file = sys.argv[i + 1]
                
                if arg in ("--output", "-out"):
                    output_file = sys.argv[i + 1]
                
                if arg == "--compress":
                    compress = True

                if arg in Arguments.OBFISCATION_METHODS:
                    obf_method = arg

            if output_file is None:
                output_file = f"obfuscated_{Path(input_file).name}"
            
            if not Path(input_file).is_file():
                ToolsConsole.error(f"Input file '{input_file}' does not exist.\n")
                ToolsConsole.examples()
                sys.exit(1)

            if not input_file.endswith(".py"):
                ToolsConsole.warn("Input file does not have a .py extension.\n")
                ToolsConsole.examples()
                sys.exit(1)

            status, result = Obfuscator(
                input_file=Path(input_file),
                output_file=Path(output_file),
                obf_method=obf_method,
                compress=compress
            ).obfuscate()

            if status:
                ToolsConsole.info("Compression enabled." if compress else "Compression disabled.")
                ToolsConsole.success(f"Obfuscated file saving to '{output_file}'.")
                ToolsConsole.save_file(result, f'output/{output_file}')
                sys.exit(0)
                
        ToolsConsole.usage()
