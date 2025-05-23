# Generated manually

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(verbose_name='消息内容')),
                ('response', models.TextField(blank=True, null=True, verbose_name='GPT回复')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('is_completed', models.BooleanField(default=False, verbose_name='是否完成')),
                ('tokens_used', models.IntegerField(default=0, verbose_name='使用的tokens数量')),
                ('model', models.CharField(default='gpt-4o', max_length=50, verbose_name='使用的模型')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.sysuser', verbose_name='用户')),
            ],
            options={
                'verbose_name': '聊天记录',
                'verbose_name_plural': '聊天记录',
                'db_table': 'chat_message',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='ChatUsage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('usage_date', models.DateField(verbose_name='使用日期')),
                ('usage_count', models.IntegerField(default=0, verbose_name='使用次数')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.sysuser', verbose_name='用户')),
            ],
            options={
                'verbose_name': '聊天使用统计',
                'verbose_name_plural': '聊天使用统计',
                'db_table': 'chat_usage',
                'unique_together': {('user', 'usage_date')},
            },
        ),
    ] 