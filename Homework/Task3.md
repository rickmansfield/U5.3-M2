# Unit 5.3 M2 Queues & Stacks Homework
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.

## Implement a queue using two stacks.

You are given an array of requests, where requests[i] can be "push <x>" or "pop". Return an array composed of the results of each "pop" operation that is performed.

Example

For requests = ["push 1", "push 2", "pop", "push 3", "pop"], the output should be
queueOnStacks(requests) = [1, 2].

After the first request, the queue is {1}; after the second it is {1, 2}. Then we do the third request, "pop", and add the first element of the queue 1 to the answer array. The queue becomes {2}. After the fourth request, the queue is {2, 3}. Then we perform "pop" again and add 2 to the answer array, and the queue becomes {3}.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string requests

requests[i] can be "push <x>" or "pop". It is guaranteed that "pop" isn't applied to an empty queue.

Guaranteed constraints:
1 ≤ requests.length ≤ 300,
-1000 ≤ x ≤ 1000.

[output] array.integer

Return an array composed of the results of each "pop" operation that is performed.