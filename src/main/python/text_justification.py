class Solution:
    def fullJustify(self, words, maxWidth) :
        width, text, result = 0, '', []
        
        # Formulate the lines without justification by using '\n' as separator between lines        
        for word in words:
            if width + len(word) <= maxWidth:
                width += len(word) + 1
                text += word + ' '
                print ("inside if")
                print (width)
                print (text)
            else:
                width = len(word) + 1
                text += '\n' + word + ' '  
                print ("inside else")
                print (width)
                print (text)   
                
        #Split the formulated lines
        lines = text.split('\n')
        # Parse the lines to justify
        for line in lines[:-1]:
            print ("line: "+line)
            justify = maxWidth - len(line) + 1 # +1 Because we are adding space after every word includes last word as well
            print ("justify: "+str(justify))
            words = line.split()
            print ("words "+str(words))
            # Calculate the space to be filled, if space cannot be equally divided among the words, calculate the space that needed to be filled
            spaces_after_word = justify // (len(words)-1) if len(words) > 1 else justify # if line contains only one word
            left_word_space = justify % (len(words)-1) if len(words) > 1 else justify # if line contains only one word
            print ("spaces_after_word: , left_word_space : "+str(spaces_after_word),str(left_word_space))
            line = ''
            # Last word should be dealt seperately because we should not add space after the last word
            print ("words[:-1] "+str(words[:-1]))
            for word in words[:-1]:
                line += word + (" " * (spaces_after_word+1))
                print ("line0: "+str(line))
                if left_word_space:
                    line += ' '
                    print ("line left: "+str(line))
                    left_word_space -= 1
            line += words[-1]
            print ("line1: "+str(line))
            
            # If there's only one word in the line justify the line
            if len(words) == 1:
                line += (' ' * justify)
            print ("line2: "+str(line))
            result.append(line)
            
        # Last line should be left justified hence treated seperately
        line = "".join(lines[-1]) # Because the last character will be space
        line = line[:-1] 
        result.append(line + (" " * (maxWidth - len(line))))
        return result
if __name__ == '__main__':
    Sol=Solution()
    words = [ "justification."]
    maxWidth = 16
    print (Sol.fullJustify(words, maxWidth))   