# PyProtect - Python Code Obfuscator

PyProtect is a powerful Python code obfuscation tool that helps protect your source code from reverse engineering and unauthorized analysis. It transforms readable Python scripts into obfuscated versions that maintain full functionality while being significantly harder to understand and decompile.

## Features

### Multiple Obfuscation Methods

- **Bytecode Obfuscation** (`--bytecode`): Converts Python source to compiled bytecode using marshal, removing all comments, docstrings, and formatting
- **Lambda Obfuscation** (`--lambda`): Uses nested lambda expressions and base64 encoding to hide code structure
- **Hybrid Obfuscation** (`--hybrid`): Combines bytecode compilation with lambda expressions for maximum obfuscation
- **Optional Compression** (`--compress`): Applies zlib compression to reduce file size and add complexity

### Key Advantages

- ✅ **Preserves Functionality**: Obfuscated code executes identically to the original
- ✅ **No External Dependencies**: Uses only Python standard library modules
- ✅ **Cross-Platform Compatible**: Works on any system with Python 3.x
- ✅ **Simple CLI Interface**: Easy-to-use command-line options
- ✅ **Random Variable Names**: Generates unique random names for variables in lambda/hybrid modes
- ✅ **Smart Encoding**: Automatically splits large encoded strings into chunks for better obfuscation

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd pyprotect

# Install dependencies (minimal, only standard library)
pip install -r requirements.txt
```

## Project Structure

```
pyprotect/
├── pyprotect.py          # Main entry point
├── src/
│   ├── obfuscator.py     # Obfuscation methods implementation
│   └── tools.py          # Utility functions and argument handling
├── output/               # Generated obfuscated files (created automatically)
├── README.md
└── requirements.txt
```

## Usage

### Basic Syntax

```bash
python pyprotect.py [options]
```

### Options

```
Options:
    --help, -h                Show this help message and exit
    --input, -in FILE         Input .py file to obfuscate
    --output, -out FILE       Output .py file (default: obfuscated_<input>)

Obfuscation Methods:
    --bytecode                Obfuscate using marshal bytecode loader
    --lambda                  Obfuscate using nested lambda expressions
    --hybrid                  Hybrid obfuscation combining bytecode and lambda
    
Additional Options:
    --compress                Enable compression (works with all methods)
```

### Examples

```bash
# Basic bytecode obfuscation
python pyprotect.py --input script.py --bytecode

# Bytecode with compression
python pyprotect.py --input script.py --output protected.py --bytecode --compress

# Lambda obfuscation
python pyprotect.py --input myapp.py --lambda

# Hybrid obfuscation with compression (maximum protection)
python pyprotect.py --input sensitive.py --hybrid --compress

# Using short flags
python pyprotect.py -in test.py -out obf_test.py --hybrid
```

## How It Works

### Bytecode Obfuscation (`--bytecode`)

1. Compiles Python source code into bytecode using `compile()`
2. Serializes bytecode with `marshal.dumps()`
3. Optionally compresses with `zlib.compress()`
4. Encodes to base64
5. Generates a compact loader that reverses the process at runtime

**Example Output:**
```python
import base64 as b, marshal as m;import zlib as z;a='<base64_data>';b=b.b64decode(a);b=z.decompress(b);c=m.loads(b);exec(c)
```

### Lambda Obfuscation (`--lambda`)

1. Encodes source code to base64
2. Optionally splits into random chunks
3. Creates nested lambda functions with random variable names
4. Generates obfuscated code that decodes and executes at runtime

**Example Output:**
```python
(lambda xkqwmzprtl: (lambda yjhgfdsakl: (lambda mnbvcxzaqw: (lambda poiuytrewq: poiuytrewq(mnbvcxzaqw(yjhgfdsakl(xkqwmzprtl))))(lambda asdfghjklz: exec(asdfghjklz)))(lambda asdfghjklz: asdfghjklz.decode('utf-8')))(lambda asdfghjklz: __import__('base64').b64decode(asdfghjklz)))('<base64_data>')
```

### Hybrid Obfuscation (`--hybrid`)

1. Compiles to bytecode (like `--bytecode`)
2. Wraps in nested lambdas (like `--lambda`)
3. Combines both techniques for maximum obfuscation
4. Supports compression for additional protection

## Security Considerations

⚠️ **Important Notes:**

- Obfuscation is **not encryption** - it makes code harder to read, not impossible
- Determined attackers with sufficient time can still reverse engineer obfuscated code
- This tool is best used as **one layer** of a comprehensive security strategy
- Always use proper encryption for truly sensitive data
- Obfuscation does not protect against runtime analysis or debugging

### Recommended Use Cases

✅ Protecting proprietary algorithms in commercial software  
✅ Preventing casual inspection of source code  
✅ Distributing Python applications while obscuring implementation details  
✅ Adding a barrier against automated code analysis tools  
✅ Securing business logic in deployed applications  

### Not Recommended For

❌ Protecting passwords, API keys, or sensitive credentials (use environment variables)  
❌ Security-critical cryptographic operations (use proper encryption)  
❌ Preventing all reverse engineering attempts (impossible with obfuscation alone)  

## Output

Obfuscated files are automatically saved to the `output/` directory with the specified filename. If no output filename is provided, the default format is `obfuscated_<original_filename>.py`.

## Requirements

- Python 3.6 or higher
- Standard library modules only (no external dependencies)

## Performance Impact

- **File Size**: Bytecode obfuscation typically increases file size by 30-40%. Compression can reduce this.
- **Runtime**: Minimal overhead - obfuscated code runs at nearly native speed after initial deobfuscation
- **Memory**: Small increase during initial loading for decompression/decoding

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## Disclaimer

This tool is provided for legitimate purposes such as protecting intellectual property in commercial software. Users are responsible for ensuring their use complies with applicable laws and regulations. The authors are not responsible for any misuse of this tool.

## Troubleshooting

**Issue**: "Input file does not exist"  
**Solution**: Verify the file path is correct and the file exists

**Issue**: "Input file does not have a .py extension"  
**Solution**: Ensure your input file ends with `.py`

**Issue**: "Invalid arguments provided"  
**Solution**: Check the syntax - you must specify an obfuscation method (--bytecode, --lambda, or --hybrid)

**Issue**: Obfuscated file doesn't run  
**Solution**: Ensure the original file runs without errors before obfuscating

## Contact

- Discord: **vihtoriax**
- telegram: **https://t.me/vihtoriadev**
