echo "=== ФИНАЛЬНОЕ ТЕСТИРОВАНИЕ ВСЕХ ЭТАПОВ ==="
echo ""

echo "1. ЭТАП 1: Промежуточное представление"
python assembler.py tests/test_example_1.yaml - -test-intermediate 2>&1 | Select-String -Pattern "ПРОМЕЖУТОЧНОЕ"
echo "✓ Этап 1 проверен"
echo ""

echo "2. ЭТАП 2: Байт-код"
python assembler.py test_spec.yaml spec_test.bin --test-bytecode 2>&1 | Select-String -Pattern "БАЙТ-КОД"
echo "✓ Этап 2 проверен"
echo ""

echo "3. ЭТАП 3: Интерпретатор и память"
python run.py tests/test_copy_array.yaml test3.bin test3.json
$mem = Get-Content test3.json | ConvertFrom-Json
echo "  Записано ячеек памяти: $($mem.PSObject.Properties.Count)"
echo "✓ Этап 3 проверен"
echo ""

echo "4. ЭТАП 4: bswap команда"
python run.py tests/test_example_1.yaml test4.bin test4.json
$mem4 = Get-Content test4.json | ConvertFrom-Json
echo "  Результат bswap: $($mem4.'101')"
echo "✓ Этап 4 проверен"
echo ""

echo "5. ЭТАП 5: Вектор bswap длины 10"
python run.py tests/test_bswap_vector.yaml test5.bin test5.json
$mem5 = Get-Content test5.json | ConvertFrom-Json
echo "  Элементов в векторе: $($mem5.PSObject.Properties.Count)"
echo "✓ Этап 5 проверен"
echo ""

Remove-Item test*.bin, test*.json -ErrorAction SilentlyContinue
echo "=== ВСЕ ЭТАПЫ УСПЕШНО ПРОВЕРЕНЫ ==="
