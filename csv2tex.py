import csv
import os.path
import sys


def tex_header(header: list) -> str:
    """
    This method builds a LaTeX header based on
    the csv list of columns. Uses booktabs environment.

    Parameters
    ----------
    header : list
        The list of column names

    Return
    ----------
        The TeX-formatted string

    """

    head = ('\\begin{table}\n'
            '\t\\centering\n'
            '\t\\caption{\\label{My awesome label} My awesome caption}\n'
            '\t\\begin{tabular}{')

    for _ in header:
        head += 'l'

    head += '}\n\t\t'
    head += '\\toprule\n\t\t'

    # Column names
    cnt = 1
    for c in header:
        if cnt < len(header):
            head += f"{c} & "
            cnt += 1
        else:
            head += f"{c} \\\\ \n"

    return head + '\t\t\\midrule\n'


def tex_footer() -> str:
    """
    This method builds a LaTeX table footer

    Return
    ----------
        The TeX-formatted string

    """

    return ('\\bottomrule \n'
            '\t\\end{tabular} \n'
            '\\end{table}')


def tex_content(reader) -> str:
    """
    This method builds the LaTeX body based on
    the csv list of rows.

    Parameters
    ----------
    reader : csvreader
        The csv reader

    Return
    ----------
    str
        The TeX-formatted string

    """

    content = '\t\t'
    cnt = 1
    for row in reader:
        for elem in row:
            if cnt < len(row):
                content += f"{elem} & "
                cnt += 1
            else:
                content += f"{elem} \\\\ \n \t\t"
        cnt = 1

    return content


def to_tex(csvfile):
    """
    This method reads a csv file and writes a
    LaTeX table with the content. The .tex file is
    saved in the same folder of the csv file with
    the same name.

    Parameters
    ----------
    csvfile : File
        The csv file to convert

    """

    tex_string = ''

    with open(csvfile) as f:
        reader = csv.reader(f)
        header = next(reader)

        tex_string += tex_header(header)
        tex_string += tex_content(reader)
        tex_string += tex_footer()

    with open(f"{csvfile.replace('.csv', '')}_converted.tex", 'w') as f:
        f.write(tex_string)
        print('Conversion successful')


def show_help():
    print('\ncsv2tex: convert your csv values in a TeX-formatted table.\n'
          '-\n'
          '- Usage: python csv2tex.py <path_to_csv_file>.csv\n'
          '-\n'
          '- If the given csv file exists, a new .tex file will be created within\n'
          '- the same directory and with the same name.\n'
          '-\n'
          '- Stefano Demarchi')


# Main entry point
if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == '-h':
            show_help()
        elif os.path.isfile(sys.argv[1]):
            to_tex(sys.argv[1])
        else:
            print('Error: incorrect file specified')
    else:
        show_help()
