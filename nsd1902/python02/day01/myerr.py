# try:
#     num = int(input('number: '))
#     result = 100 / num
#     print(result)
#     print('Done')
# except ValueError:
#     print('无效的输入')
# except ZeroDivisionError:
#     print('无效的输入')
# except KeyboardInterrupt:
#     print('\nBye-bye')
# except EOFError:
#     print('\nBye-bye')


# try:
#     num = int(input('number: '))
#     result = 100 / num
#     print(result)
#     print('Done')
# except (ValueError, ZeroDivisionError):
#     print('无效的输入')
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')


try:
    num = int(input('number: '))
    result = 100 / num
except (ValueError, ZeroDivisionError):
    print('无效的输入')
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
    exit(65)
else:
    print(result)
finally:
    print('Done')

print('正常结束')
