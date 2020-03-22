# This file will work with serialzers
from rest_framework import serializers

# Bring the post model we created into our serializers
from .models import Post

# This is very similar on how we construct a form
# from django improt forms
# class PostForm(forms.ModelForm)
#   class Meta:
#       model = Post
#       fields = (
#       'title', 'description
#       )


# This post serializer represents a transformation from psot model into JSON payload with the fields given,
# In the backend it looks at what the fields are and looks how it can seralize those fields,
# We don't need to use the JSON package and dumping into JSON
# Now we can use the serializers in a view
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title','description'
        )
