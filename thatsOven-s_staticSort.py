# Copyright(C) 2020 thatsOven
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
def insertion_sort(InputList, n):
    for i in range(1, n):
        j = i-1
        nxt_element = InputList[i]
        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j+1] = InputList[j]
            j=j-1
        InputList[j+1] = nxt_element
from itertools import chain
def thatsOvens_staticSort(a):
    M = max(a)
    size = len(a)
    constant = M/(size+4)
    counter = 0
    listcount = 0
    while listcount < size:
        if type(a[counter]) is list:
            counter += 1
        else:
            if int(a[counter]*constant) == counter:
                a[counter] = [a[counter]]
            else:
                if type(a[int(a[counter]*constant)]) is list:
                    a[int(a[counter]*constant)].append(a[counter])
                    a[counter] = []
                else:
                    a[int(a[counter]*constant)], a[counter] = [a[counter]], a[int(a[counter]*constant)]
            listcount += 1 
    for i in range(len(a)):
        lt = len(a[i])
        if lt > 1:
            insertion_sort(a[i], lt)
    return list(chain.from_iterable(a))
