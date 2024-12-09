#!/usr/bin/env nextflow

params.input_str = "Hello World"

process convertToCaps {
    input:
    val input_string

    output:
    path 'output.txt'

    script:
    """
    echo "$input_string" | tr '[:lower:]' '[:upper:]' > output.txt
    """
}

workflow {
    convertToCaps(params.input_str)
}