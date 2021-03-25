import os

class _CppInfo(object):
    def __init__(self):
        self.includedirs = []
        self._include_paths = None
        self.rootpath = ""
        self.filter_empty = True

    def _filter_paths(self, paths):
        abs_paths = [os.path.join(self.rootpath, p)
                     if not os.path.isabs(p) else p for p in paths]
        if self.filter_empty:
            return [p for p in abs_paths if os.path.isdir(p)]
        else:
            return abs_paths
        
    @property
    def include_paths(self):
        if self._include_paths is None:
            self._include_paths = self._filter_paths(self.includedirs)
        return self._include_paths
        
class CppInfo(_CppInfo):
    def __init__(self, root_folder):
        super(CppInfo, self).__init__()
        self.rootpath = root_folder  # the full path of the package in which the conans is found         
     
        
if __name__ == "__main__":
    cppinfo = CppInfo(".")
    cppinfo.includedirs = ['include']
    cppinfo.includedirs = ['D:\\test']
    cppinfo.include_paths.append('include')
    print cppinfo.include_paths