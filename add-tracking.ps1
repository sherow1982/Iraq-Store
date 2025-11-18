# PowerShell Script to add Google Analytics and Tag Manager to all product pages
# Run this in PowerShell from repository root

Write-Host "📊 Adding Google Analytics & Tag Manager to all products..." -ForegroundColor Cyan

$gtmHead = @'
    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-TVV3GQZZ');</script>
    <!-- End Google Tag Manager -->

    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-CGC2RV7T45"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-CGC2RV7T45');
    </script>

'@

$gtmBody = @'
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TVV3GQZZ"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <!-- End Google Tag Manager (noscript) -->

'@

$files = Get-ChildItem -Path "products" -Filter "*.html" -File
$count = 0

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    
    # Skip if already has tracking
    if ($content -match 'GTM-TVV3GQZZ') {
        Write-Host "✅ Already tracked: $($file.Name)" -ForegroundColor Yellow
        continue
    }
    
    # Add GTM to <head> (after <head> tag)
    $content = $content -replace '(<head>)', "`$1`n$gtmHead"
    
    # Add GTM noscript to <body> (after <body> tag)
    $content = $content -replace '(<body>)', "`$1`n$gtmBody"
    
    Set-Content -Path $file.FullName -Value $content -Encoding UTF8 -NoNewline
    $count++
    Write-Host "✅ Added tracking: $($file.Name)" -ForegroundColor Green
}

Write-Host ""
Write-Host "✅ Done! Added tracking to $count files." -ForegroundColor Green
Write-Host ""
Write-Host "🚀 Now commit and push:" -ForegroundColor Yellow
Write-Host "   git add products/" -ForegroundColor White
Write-Host "   git commit -m 'Add Google Analytics and Tag Manager to all products'" -ForegroundColor White
Write-Host "   git push origin main" -ForegroundColor White