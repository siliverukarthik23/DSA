class Solution:
    def maxFreqSum(self, s: str) -> int:
        vm=0
        cm=0
        vd={}
        cd={}
        for i in s:
            if i in 'aeiou':
                if i not in vd:
                    vd[i]=1
                    vm=max(vd[i],vm)
                else:
                    vd[i]+=1
                    vm=max(vm,vd[i])
            else:
                if i not in cd:
                    cd[i]=1
                    cm=max(cd[i],cm)
                else:
                    cd[i]+=1
                    cm=max(cm,cd[i])
        return vm+cm