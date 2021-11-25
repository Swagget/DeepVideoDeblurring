# function checkDir(path2outputs)
#
# if ~exist(path2outputs, 'dir')
#     mkdir(path2outputs);
# end

import os
def checkDir(path2outputs):
    if not os.path.isdir(path2outputs):
        os.mkdir(path2outputs)