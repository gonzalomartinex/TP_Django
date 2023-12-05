# Generated by Django 4.2.4 on 2023-11-10 11:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caracteristicas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caracteristica', models.CharField(max_length=50)),
                ('detalle', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_plan', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoTarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_tarjeta', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('contraseña', models.CharField(max_length=50)),
                ('estado', models.BooleanField()),
                ('fecha_inicio', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.IntegerField()),
                ('descripcion', models.TextField(max_length=250)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Streaming.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTitular', models.CharField(max_length=255)),
                ('apellidoTitular', models.CharField(max_length=255)),
                ('numero_tarjeta', models.BigIntegerField()),
                ('fecha_vencimiento', models.DateField()),
                ('codigo_seguridad', models.IntegerField()),
                ('TipoTarjeta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Streaming.tipotarjeta')),
            ],
        ),
        migrations.CreateModel(
            name='Suscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_suscripcion', models.DateField(default=django.utils.timezone.now)),
                ('SusActiva', models.BooleanField()),
                ('id_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Streaming.plan')),
                ('id_tarjeta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Streaming.tarjeta')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Streaming.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='plan',
            name='tipo_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Streaming.tipoplan'),
        ),
        migrations.CreateModel(
            name='CaracteristicasXPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esta_activo', models.BooleanField()),
                ('cantidad', models.IntegerField()),
                ('descripcion', models.TextField(max_length=250)),
                ('caracteristica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Streaming.caracteristicas')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Streaming.plan')),
            ],
        ),
    ]
