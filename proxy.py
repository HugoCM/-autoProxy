
"""
命令行学校代理设置

Usage:
    proxy [-of] 
    
Options:
    -h,--help   显示帮助菜单
    -o          开启代理
    -f          关闭代理

Example:
    proxy -o
    proxy -f
"""

from docopt import docopt
import regeditor

offsets = {'-o':'On','-f':'Off'}
class InvalidInputError(Exception):

    """Error in construction of input by developer."""
    
def cli():
    """command-line interface"""
    arguments = docopt(__doc__)
    offset = ''.join([
        key for key, value in arguments.items() if value is True
    ])
    if (offset != '-o') and (offset != '-f'):
        raise InvalidInputError('input should be -o or -f')
        offset = 'input should be -o or -f'
    print(offset)
    opt = offsets.get(offset)
    regeditor.set(opt)
    
if __name__ == '__main__':
    cli()