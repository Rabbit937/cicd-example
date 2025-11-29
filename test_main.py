def test_main():
    """测试 main.py 中的函数."""
    from main import main
    import io
    import sys
    
    # 捕获 main 函数的输出
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    main()
    
    # 恢复 stdout
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue().strip()
    assert output == "Hello from cicd-example!"