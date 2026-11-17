param(
    [int]$Port = 8501
)

$pythonPath = 'D:\Python313\python.exe'
if (-not (Test-Path -LiteralPath $pythonPath)) {
    $pythonPath = (Get-Command python -ErrorAction Stop).Source
}

# Keeps the dashboard reliable on machines with limited BLAS thread resources.
$env:OPENBLAS_NUM_THREADS = '1'
& $pythonPath -m streamlit run app.py --server.port $Port
