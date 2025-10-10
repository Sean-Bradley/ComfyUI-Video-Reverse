class VideoReverseNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "frames": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "reverse"
    CATEGORY = "SBCODE"

    def reverse(self, frames):
        if frames is None or len(frames) == 0:
            return {}

        frames.reverse()

        print("The video frames have now been reversed.")

        return (frames,)


NODE_CLASS_MAPPINGS = {"VideoReverseNode": VideoReverseNode}
NODE_DISPLAY_NAME_MAPPINGS = {"VideoReverseNode": "Video Reverse"}
