%if res:
<h2>
  Success!
</h2>
<p>
  An invitation has been sent to your Jabber ID. When accepted, you
  will receive instant messages from the organizers during the
  meeting.
</p>
<p>
  Thank you.
</p>

%else:
<h2>
  Failure!
</h2>
<p>
  A problem has occurred with your Jabber account. The system could
  not send you an invitation. Please, contact the organizers!
</p>
<p>
  Thank you.
</p>

%end

%rebase base author=author, email=email
