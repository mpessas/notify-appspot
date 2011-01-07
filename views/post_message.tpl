%if sent:
<p class="result">Message sent.</p>
%end
<h2>Post a message</h2>
<form method="POST">
  <label for="msg">
    Message:
  </label>
  <input type="text" name="msg" placeholder="Message" />
  <input type="submit" value="Send" />
</form>
%rebase base author=author, email=email
