class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for curr in path.split("/"):
            if stack and curr == "..":
                stack.pop()
            elif curr not in [".", "", ".."]:
                stack.append(curr)
        return "/" + "/".join(stack)