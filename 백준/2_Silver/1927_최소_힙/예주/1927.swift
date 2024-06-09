
import Foundation

func sol1927_() {
    
    struct Heap<T: Comparable> {
        private var elements: [T] = []
        private let comparer: (T, T) -> Bool
        
        init(comparer: @escaping (T,T) -> Bool) {
            self.comparer = comparer
        }
        
        mutating func insert(element: T) {
            if elements.isEmpty {
                elements.append(element)
                elements.append(element)
                return
            }
            
            elements.append(element)
            swimUp(index: elements.count - 1)
        }
        
        mutating func pop() -> T? {
            if elements.count <= 1 { return nil }
            elements.swapAt(1, elements.count - 1)
            let deletedElement = elements.removeLast()
            swimDown(index: 1)
            return deletedElement
        }
        
        mutating private func swimUp(index: Int) {
            // 자식노드 > 부모노드 라면 swap
            // 루트노드면 반복문 탈출 index > 1
            var index = index
            while index > 1 && comparer(elements[index], elements[index / 2]) {
                elements.swapAt(index, index / 2)
                index /= 2
            }
        }
        
        mutating private func swimDown(index: Int) {
            var swapIndex = index
            var isSwap = false
            let leftIndex = index * 2
            let rightIndex = (index * 2) + 1
            
            if leftIndex < elements.endIndex && comparer(elements[leftIndex], elements[swapIndex]) {
                swapIndex = leftIndex
                isSwap = true
            }
            
            
            if rightIndex < elements.endIndex && comparer(elements[rightIndex], elements[swapIndex]) {
                swapIndex = rightIndex
                isSwap = true
            }
            
            if isSwap {
                elements.swapAt(swapIndex, index)
                swimDown(index: swapIndex)
            }
        }
    }
    
    var minHeap = Heap<Int>(comparer: <)
    
    let input = Int(readLine()!)!
    
    for _ in 0..<input {
        let x = Int(readLine()!)!
        if x == 0 {
            print(minHeap.pop() ?? 0)
        } else {
            minHeap.insert(element: x)
        }
    }
}

//sol1927_()
