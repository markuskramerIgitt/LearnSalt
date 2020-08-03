import subprocess
import sys
import salt_chcp
import salt_init
import salt_stringutils


def run_and_return_byte_stream(cmd):
    completed_process = subprocess.run(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    stdout_bytes = completed_process.stdout
    return stdout_bytes


def run_and_decode_by_current_code_page(cmd):
    # Robust decode according to known code page
    # Robust means: replace non-decodeable character with numeric value
    # Not robust means: any non-decodeable character prevents decoding of the whole byte stream
    # robust values for errors: ignore  backslashreplace
    # ascii is only robust in combination with errors="backslashreplace"
    #
    # Get byte stream
    stdout_bytes = run_and_return_byte_stream(cmd)
    #
    #
    print("######## Collect hints for encoding")
    #
    print("### __salt_system_encoding__ = {}".format(__salt_system_encoding__))
    # sys.getdefaultencoding not useful, because always utf-8
    print("### sys.getdefaultencoding = {}".format(sys.getdefaultencoding()))
    # Detect the current code page
    code_page = salt_chcp.chcp()
    print("### code_page = {}".format(code_page))
    assumend_encoding = "ascii"
    # Select encoding by current code page
    encoding_by_code_page = {
        "437": "cp437",
        "850": "cp850",
        "1252": "cp1252",
        "65001": "utf-8",
    }
    if code_page in encoding_by_code_page:
        assumend_encoding = encoding_by_code_page[code_page]
    print("### assumend_encoding = {}".format(assumend_encoding))
    if len(sys.argv) == 2:
        assumend_encoding = sys.argv[1]
        print("###  encoding from commandline = {}".format(assumend_encoding))
    ret_string = stdout_bytes.decode(assumend_encoding, errors="backslashreplace")
    return ret_string


# print(run_and_decode_by_current_code_page("sc.exe query power"))

print("############# Decode by code page")
print(run_and_decode_by_current_code_page("dir /b test*"))

print("############# Decode by Salt")
print(salt_stringutils.to_unicode(run_and_return_byte_stream("dir /b test*")))
