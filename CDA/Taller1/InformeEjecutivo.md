# Informe Ejecutivo

# Objetivo
Este informe tiene como propósito ofrecer a las cadenas hoteleras un conjunto de estrategias de gestión enfocadas en cuatro dimensiones clave: tipo de cliente, tarifa promedio diaria, tipo de hotel y tiempo de anticipación de la reserva. El objetivo principal es reducir el número de cancelaciones y optimizar la administración de la agenda hotelera.

# Insights

## 1. Tipo de Cliente

![TipoCliente_Tasacancelaciones](figs/TipoCliente_vs_cancelacion.png)

<figcaption style="font-size: 0.95rem; color: #555;">
<strong>Figura 1.</strong> Tipo de cliente vs. cancelación.
</figcaption>

El tipo de cliente es un factor determinante para comprender y anticipar los patrones de cancelación dentro de la cadena hotelera. Los clientes **Transient**, tanto individuales como en la modalidad **Transient-Party**, concentran el mayor volumen de reservas y, al mismo tiempo, exhiben las tasas de cancelación más elevadas. En particular, los Transient individuales alcanzan una tasa del **46.8%**, lo que se traduce en más de **18,000 cancelaciones absolutas**, constituyéndose así en el segmento de mayor riesgo tanto operativo como financiero. Esta situación exige una estrategia específica para reducir la incertidumbre y mejorar la estabilidad en la gestión de la demanda.

Para este grupo se proponen políticas de cancelación diferenciadas, que permitan mitigar la volatilidad de sus decisiones. Entre las medidas más efectivas se encuentran la implementación de tarifas no reembolsables con incentivos, que ofrezcan precios más bajos o beneficios adicionales a cambio del compromiso de permanencia, así como la exigencia de un pago anticipado parcial que disminuya las cancelaciones impulsivas y refuerce la seriedad de la reserva. Estas acciones no solo reducen la pérdida de ingresos por cancelaciones tardías, sino que también incrementan la previsibilidad en la planificación de ocupación.

Por otra parte, los clientes **Contract** y **Group** muestran un comportamiento mucho más estable, con tasas de cancelación significativamente menores (**0.133** y **0.115**, respectivamente). Estos segmentos, aunque representan un porcentaje reducido del total de reservas, son estratégicamente valiosos por la fiabilidad que aportan. En este caso, la cadena hotelera debería mantener y fortalecer los acuerdos comerciales existentes, reforzando convenios corporativos y grupales que ya demuestran alta retención. Adicionalmente, se recomienda implementar programas de beneficios exclusivos, como descuentos por volumen o mejoras de categoría (upgrades), que aseguren la continuidad de estas reservas y fortalezcan las relaciones a largo plazo con empresas y colectivos.


## 2. Tarifa promedio diario (ADR) 

![ADR](figs/ADR_vs_cancelacion_1.png)
<figcaption style="font-size: 0.95rem; color: #555;">
<strong>Figura 2.</strong> Distribución de tarifas (ADR) vs. cancelación.
</figcaption>
<br>

<img src="figs/ADR_vs_cancelacion_2.png" alt="ADR" width="300">
<figcaption style="font-size: 0.95rem; color: #555;">
<strong>Figura 3.</strong> Rango de tarifas (ADR) vs. cancelación.
</figcaption>

Un factor determinante en el comportamiento de cancelación es el **nivel de precios**. Un análisis estadístico (prueba t-student) confirmó una diferencia significativa en las tarifas promedio (ADR) entre las reservas que se cancelaron y las que se mantuvieron. Los datos revelaron un patrón claro: a medida que la tarifa diaria promedio aumenta, también lo hace la probabilidad de cancelación. Específicamente, las reservas con tarifas bajas (0-59) tienen la tasa de cancelación más baja (23.1%). Los segmentos intermedios (59-81 y 81-115) muestran tasas crecientes (42% y 46.8%, respectivamente), mientras que el segmento de tarifas más altas (115-210) registra la tasa más elevada (52.9%).


Ante este comportamiento, las **estrategias de gestión de tarifas** deben ajustarse a cada segmento de ADR. En el segmento bajo (0-59), se recomienda mantener la competitividad con precios accesibles y programas de fidelización sencillos. Además, se pueden ofrecer servicios adicionales de bajo costo a través de un *upselling* simple. Para los segmentos intermedios (59-115), es conveniente ofrecer flexibilidad en las cancelaciones, aplicar promociones dinámicas en temporadas de baja demanda e incorporar seguros de cancelación para mitigar la percepción de riesgo del cliente. Finalmente, en el segmento alto (115-210), la estrategia se basa en políticas de cancelación más estrictas, como opciones no reembolsables o de prepago. En este caso, el precio elevado debe justificarse con un valor agregado tangible y un servicio personalizado que refuerce la exclusividad y, a la vez, reduzca la probabilidad de cancelación.



## 3. Tiempo de anticipación 

![ lead_time](figs/leadtime_vs_cancelaciones.png)
<figcaption style="font-size: 0.95rem; color: #555;">
<strong>Figura 4.</strong> Tiempo de anticipación vs. cancelación.
</figcaption>


El análisis confirma que el tiempo de anticipación (lead_time) es el principal predictor de cancelaciones, con una correlación positiva significativa (r=0.247 - Pearson, r=0.290 - Spearman). Las reservas realizadas con más de seis meses de antelación concentran la mayor proporción de cancelaciones, mientras que aquellas efectuadas con una semana o menos muestran un riesgo considerablemente menor, diferencia validada estadísticamente (p<0.001). Esto implica que, aunque las reservas de largo plazo ofrecen mayor visibilidad de la demanda, también exigen políticas de gestión de riesgo más estrictas para mitigar su elevada volatilidad.


## 4. Tipo de Hotel
![tipo de hotel](figs/TipoHotel_vs_cancelacion.png)
<figcaption style="font-size: 0.95rem; color: #555;">
<strong>Figura 5.</strong> Tipo de hotel vs. cancelación.
</figcaption>


El análisis muestra que City Hotels y Resort Hotels operan como dos negocios claramente distintos en términos de cancelaciones. Los City Hotels presentan una tasa cercana al 70%, lo que refleja alta volatilidad. En contraste, los Resort Hotels registran un 25%, con marcada estabilidad. La diferencia de 45 puntos porcentuales es estadísticamente significativa (p<0.001). Este hallazgo exige estrategias diferenciadas: los City Hotels requieren una gestión de riesgo intensiva, mientras que los Resort Hotels pueden enfocarse en maximizar el valor por cliente.