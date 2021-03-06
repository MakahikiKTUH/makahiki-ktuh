# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CategoryGrid'
        db.create_table('smartgrid_categorygrid', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('level', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['smartgrid.Level'])),
            ('column', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['smartgrid.Category'])),
        ))
        db.send_create_signal('smartgrid', ['CategoryGrid'])

        # Adding model 'Grid'
        db.create_table('smartgrid_grid', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('level', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['smartgrid.Level'])),
            ('column', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('row', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('action', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['smartgrid.Action'])),
        ))
        db.send_create_signal('smartgrid', ['Grid'])

        # Deleting field 'Action.category'
        db.delete_column('smartgrid_action', 'category_id')

        # Deleting field 'Action.priority'
        db.delete_column('smartgrid_action', 'priority')

        # Deleting field 'Action.level'
        db.delete_column('smartgrid_action', 'level_id')

        # Deleting field 'Category.priority'
        db.delete_column('smartgrid_category', 'priority')


    def backwards(self, orm):
        
        # Deleting model 'CategoryGrid'
        db.delete_table('smartgrid_categorygrid')

        # Deleting model 'Grid'
        db.delete_table('smartgrid_grid')

        # Adding field 'Action.category'
        db.add_column('smartgrid_action', 'category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['smartgrid.Category'], null=True, blank=True), keep_default=False)

        # Adding field 'Action.priority'
        db.add_column('smartgrid_action', 'priority', self.gf('django.db.models.fields.IntegerField')(default=1000), keep_default=False)

        # Adding field 'Action.level'
        db.add_column('smartgrid_action', 'level', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['smartgrid.Level'], null=True, blank=True), keep_default=False)

        # Adding field 'Category.priority'
        db.add_column('smartgrid_category', 'priority', self.gf('django.db.models.fields.IntegerField')(default=1), keep_default=False)


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 4, 14, 7, 5, 41, 925049)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 4, 14, 7, 5, 41, 924968)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'notifications.usernotification': {
            'Meta': {'object_name': 'UserNotification'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'contents': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'display_alert': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '20'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'unread': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'score_mgr.pointstransaction': {
            'Meta': {'ordering': "('-transaction_date',)", 'unique_together': "(('user', 'transaction_date', 'message'),)", 'object_name': 'PointsTransaction'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {}),
            'transaction_date': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'smartgrid.action': {
            'Meta': {'object_name': 'Action'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'embedded_widget': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'expire_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'point_value': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pub_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(2013, 4, 14)'}),
            'related_resource': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'social_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'unlock_condition': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'unlock_condition_text': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'through': "orm['smartgrid.ActionMember']", 'symmetrical': 'False'}),
            'video_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'video_source': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        'smartgrid.actionmember': {
            'Meta': {'unique_together': "(('user', 'action', 'submission_date'),)", 'object_name': 'ActionMember'},
            'action': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['smartgrid.Action']"}),
            'admin_comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'admin_link': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'approval_status': ('django.db.models.fields.CharField', [], {'default': "'pending'", 'max_length': '20'}),
            'award_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'completion_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '1024', 'blank': 'True'}),
            'points_awarded': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['smartgrid.TextPromptQuestion']", 'null': 'True', 'blank': 'True'}),
            'response': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'social_bonus_awarded': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_email': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'submission_date': ('django.db.models.fields.DateTimeField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'smartgrid.activity': {
            'Meta': {'object_name': 'Activity', '_ormbases': ['smartgrid.Action']},
            'action_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['smartgrid.Action']", 'unique': 'True', 'primary_key': 'True'}),
            'admin_note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'confirm_prompt': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'confirm_type': ('django.db.models.fields.CharField', [], {'default': "'text'", 'max_length': '20'}),
            'expected_duration': ('django.db.models.fields.IntegerField', [], {}),
            'point_range_end': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'point_range_start': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'smartgrid.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'db_index': 'True'})
        },
        'smartgrid.categorygrid': {
            'Meta': {'object_name': 'CategoryGrid'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['smartgrid.Category']"}),
            'column': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['smartgrid.Level']"})
        },
        'smartgrid.commitment': {
            'Meta': {'object_name': 'Commitment', '_ormbases': ['smartgrid.Action']},
            'action_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['smartgrid.Action']", 'unique': 'True', 'primary_key': 'True'}),
            'commitment_length': ('django.db.models.fields.IntegerField', [], {'default': '5'})
        },
        'smartgrid.confirmationcode': {
            'Meta': {'object_name': 'ConfirmationCode'},
            'action': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['smartgrid.Action']"}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 4, 14, 7, 5, 41, 466957)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'printed_or_distributed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'smartgrid.emailreminder': {
            'Meta': {'unique_together': "(('user', 'action'),)", 'object_name': 'EmailReminder'},
            'action': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['smartgrid.Action']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'send_at': ('django.db.models.fields.DateTimeField', [], {}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'smartgrid.event': {
            'Meta': {'object_name': 'Event', '_ormbases': ['smartgrid.Action']},
            'action_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['smartgrid.Action']", 'unique': 'True', 'primary_key': 'True'}),
            'event_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'event_location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'event_max_seat': ('django.db.models.fields.IntegerField', [], {'default': '1000'}),
            'expected_duration': ('django.db.models.fields.IntegerField', [], {})
        },
        'smartgrid.filler': {
            'Meta': {'object_name': 'Filler', '_ormbases': ['smartgrid.Action']},
            'action_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['smartgrid.Action']", 'unique': 'True', 'primary_key': 'True'})
        },
        'smartgrid.grid': {
            'Meta': {'ordering': "('level', 'column', 'row')", 'object_name': 'Grid'},
            'action': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['smartgrid.Action']"}),
            'column': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['smartgrid.Level']"}),
            'row': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'smartgrid.level': {
            'Meta': {'ordering': "('priority',)", 'object_name': 'Level'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'db_index': 'True'}),
            'unlock_condition': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'unlock_condition_text': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'})
        },
        'smartgrid.questionchoice': {
            'Meta': {'object_name': 'QuestionChoice'},
            'action': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['smartgrid.Action']"}),
            'choice': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['smartgrid.TextPromptQuestion']"})
        },
        'smartgrid.textpromptquestion': {
            'Meta': {'object_name': 'TextPromptQuestion'},
            'action': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['smartgrid.Action']"}),
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {})
        },
        'smartgrid.textreminder': {
            'Meta': {'unique_together': "(('user', 'action'),)", 'object_name': 'TextReminder'},
            'action': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['smartgrid.Action']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'send_at': ('django.db.models.fields.DateTimeField', [], {}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'text_carrier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'text_number': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['smartgrid']
