Write-Host "Installing dependencies..."

pip install -r requirements.txt

if ($LASTEXITCODE -ne 0) {
    Write-Host "Dependency installation failed!"
    exit 1
}

Write-Host "Running tests..."

pytest --html=reports/report.html --self-contained-html

if ($LASTEXITCODE -ne 0) {
    Write-Host "Tests failed!"
    exit 1
}

Write-Host "Pipeline completed successfully!"